"""
model_detect.py — Auto-detect Ollama or LM Studio running locally.

Tries Ollama first (port 11434), then LM Studio (port 1234).
Returns the backend URL and type, or raises a plain-English error.
"""

import httpx

OLLAMA_BASE = "http://localhost:11434"
LMSTUDIO_BASE = "http://localhost:1234"

TIMEOUT = 3.0  # seconds


async def detect_backend() -> dict:
    """
    Try Ollama first, then LM Studio.
    Returns {"type": "ollama"|"lmstudio", "base_url": str, "models": list[str]}
    Raises RuntimeError with a plain-English message if neither is running.
    """
    # Try Ollama
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.get(f"{OLLAMA_BASE}/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                models = [m["name"] for m in data.get("models", [])]
                return {"type": "ollama", "base_url": OLLAMA_BASE, "models": models}
    except Exception:
        pass

    # Try LM Studio (OpenAI-compatible endpoint)
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.get(f"{LMSTUDIO_BASE}/v1/models")
            if resp.status_code == 200:
                data = resp.json()
                models = [m["id"] for m in data.get("data", [])]
                return {"type": "lmstudio", "base_url": LMSTUDIO_BASE, "models": models}
    except Exception:
        pass

    raise RuntimeError(
        "No local AI model server found. "
        "Ollama is not running on port 11434 and LM Studio is not running on port 1234. "
        "Please start Ollama (run 'ollama serve' in a terminal) or open LM Studio and load a model, "
        "then refresh this page."
    )


async def get_available_models() -> dict:
    """
    Returns backend info including available model names.
    Plain-English error if nothing is running.
    """
    return await detect_backend()


def pick_best_model(models: list[str], preferred: list[str]) -> str | None:
    """
    Given a list of available models and a preference list,
    return the first preferred model that is available.
    Returns None if none of the preferred models are available.
    """
    available_lower = {m.lower(): m for m in models}
    for pref in preferred:
        # Exact match first
        if pref in models:
            return pref
        # Case-insensitive match
        if pref.lower() in available_lower:
            return available_lower[pref.lower()]
        # Prefix match (e.g. "gemma3" matches "gemma3:12b")
        for model in models:
            if model.lower().startswith(pref.lower()):
                return model
    return None
