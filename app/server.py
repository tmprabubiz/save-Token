"""
server.py — FastAPI backend for Save Token.

Endpoints:
  POST /compress  — compress text using local model
  POST /expand    — expand caveman text to readable English
  GET  /models    — list available models
  GET  /health    — check if local model backend is running

Serves the frontend from /frontend/ directory.
Run with: python app/server.py
Then open: http://localhost:8000
"""

import sys
import os
import subprocess
import platform
from pathlib import Path

# Add repo root to path so imports work when running from any directory
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.compress import build_compress_messages, calculate_savings
from app.expand import build_expand_messages
from app.model_detect import detect_backend, get_available_models
from app.router import pick_model
from app import logger as session_logger

app = FastAPI(title="Save Token", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
FRONTEND_DIR = REPO_ROOT / "frontend"
MODELS_DIR = REPO_ROOT / "models"
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


# ── Request / Response models ────────────────────────────────────────────────

class CompressRequest(BaseModel):
    text: str
    mode: str = "full"           # lite / full / ultra / wenyan-lite / wenyan-full / wenyan-ultra
    personalisation: str = ""


class CompressResponse(BaseModel):
    compressed: str
    original_words: int
    compressed_words: int
    words_saved: int
    percent_saved: int
    model_used: str
    route: str
    route_reason: str


class ExpandRequest(BaseModel):
    text: str


class ExpandResponse(BaseModel):
    expanded: str
    model_used: str


# ── Helper: call local model ─────────────────────────────────────────────────

async def call_model(base_url: str, backend_type: str, model: str, messages: list[dict]) -> str:
    """
    Call the local model (Ollama or LM Studio) with a messages array.
    Returns the assistant's reply as a plain string.
    Raises a plain-English RuntimeError on failure.
    """
    timeout = 120.0  # seconds — local models can be slow

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            if backend_type == "ollama":
                payload = {
                    "model": model,
                    "messages": messages,
                    "stream": False,
                }
                resp = await client.post(f"{base_url}/api/chat", json=payload)
                resp.raise_for_status()
                data = resp.json()
                return data["message"]["content"].strip()

            elif backend_type == "lmstudio":
                # LM Studio uses OpenAI-compatible API
                payload = {
                    "model": model,
                    "messages": messages,
                    "stream": False,
                }
                resp = await client.post(f"{base_url}/v1/chat/completions", json=payload)
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"].strip()

            else:
                raise RuntimeError(f"Unknown backend type: {backend_type}")

    except httpx.TimeoutException:
        raise RuntimeError(
            f"The local model took too long to respond. "
            f"This can happen when the model is loading for the first time. "
            f"Please wait a moment and try again."
        )
    except httpx.HTTPStatusError as e:
        raise RuntimeError(
            f"The local model returned an error (status {e.response.status_code}). "
            f"Please check that your model is loaded and try again."
        )
    except Exception as e:
        raise RuntimeError(
            f"Could not reach the local model. "
            f"Please make sure Ollama is running and your model is downloaded. "
            f"Details: {str(e)}"
        )


# ── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    """Serve the frontend index.html."""
    index_path = FRONTEND_DIR / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    return JSONResponse({"message": "Save Token API is running. Frontend not found."})


@app.get("/model-persona/{filename}")
async def model_persona(filename: str):
    """Serve a model personalisation .md file from the models/ directory."""
    # Sanitise filename — allow only .md files, no path traversal
    safe_name = Path(filename).name
    if not safe_name.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files are served here.")
    persona_path = MODELS_DIR / safe_name
    if not persona_path.exists():
        raise HTTPException(status_code=404, detail=f"Personalisation file '{safe_name}' not found.")
    return FileResponse(str(persona_path), media_type="text/plain; charset=utf-8")


@app.get("/health")
async def health():
    """Check if a local model backend is running."""
    try:
        backend = await detect_backend()
        return {
            "status": "ok",
            "backend": backend["type"],
            "base_url": backend["base_url"],
            "models": backend["models"],
            "message": f"Connected to {backend['type']} with {len(backend['models'])} model(s) available.",
        }
    except RuntimeError as e:
        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "message": str(e),
            },
        )


@app.get("/models")
async def models():
    """Return available models from Ollama or LM Studio."""
    try:
        backend = await get_available_models()
        return {
            "backend": backend["type"],
            "models": backend["models"],
        }
    except RuntimeError as e:
        return JSONResponse(
            status_code=503,
            content={"error": str(e)},
        )


@app.post("/compress", response_model=CompressResponse)
async def compress(req: CompressRequest):
    """
    Compress verbose text into token-efficient caveman style.
    Returns original and compressed text with word counts.
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        backend = await detect_backend()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    try:
        model, route, reason = pick_model(req.text, backend["models"])
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    messages = build_compress_messages(req.text, req.mode, req.personalisation)

    try:
        compressed = await call_model(backend["base_url"], backend["type"], model, messages)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    savings = calculate_savings(req.text, compressed)

    # Log the compression
    try:
        session_logger.log_compress(
            original=req.text,
            compressed=compressed,
            model_used=model,
            words_saved=savings["words_saved"],
            percent_saved=savings["percent_saved"],
        )
    except Exception:
        pass

    return CompressResponse(
        compressed=compressed,
        original_words=savings["original_words"],
        compressed_words=savings["compressed_words"],
        words_saved=savings["words_saved"],
        percent_saved=savings["percent_saved"],
        model_used=model,
        route=route,
        route_reason=reason,
    )


@app.post("/expand", response_model=ExpandResponse)
async def expand(req: ExpandRequest):
    """
    Expand caveman-style text back to clear, readable English.
    Logs the expansion result.
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        backend = await detect_backend()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    try:
        model, route, reason = pick_model(req.text, backend["models"])
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    messages = build_expand_messages(req.text)

    try:
        expanded = await call_model(backend["base_url"], backend["type"], model, messages)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    # Log the expansion
    try:
        session_logger.log_expand(
            compressed_input=req.text,
            expanded=expanded,
            model_used=model,
        )
    except Exception:
        pass  # Never let logging errors crash the app

    return ExpandResponse(expanded=expanded, model_used=model)


@app.post("/open-logs")
async def open_logs():
    """Open the logs folder in the system file explorer."""
    logs_path = REPO_ROOT / "logs"
    logs_path.mkdir(exist_ok=True)
    try:
        system = platform.system()
        if system == "Windows":
            subprocess.Popen(f'explorer "{logs_path}"')
        elif system == "Darwin":
            subprocess.Popen(["open", str(logs_path)])
        else:
            subprocess.Popen(["xdg-open", str(logs_path)])
        return {"status": "ok", "path": str(logs_path)}
    except Exception:
        return JSONResponse(status_code=500, content={"error": "Could not open logs folder. Find it manually at: save-Token/logs/"})

# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Reset session log on startup
    session_logger.reset_session()

    print("💰 Save Token starting...")
    print("   Open your browser at: http://localhost:8000")
    print("   Press Ctrl+C to stop.")
    print()

    uvicorn.run(
        "app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="warning",
    )
