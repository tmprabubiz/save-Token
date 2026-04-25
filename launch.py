"""
launch.py — Launch Save Token as a standalone desktop window.

Usage:
  python launch.py

This opens the app in a native window (not a browser tab).
The window appears in the Windows taskbar when minimised.
"""

import threading
import time
import sys
from pathlib import Path

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent))

import uvicorn
import webview
from app import logger as session_logger

def start_server():
    uvicorn.run(
        "app.server:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="warning",
    )

if __name__ == "__main__":
    # Reset session log on startup
    session_logger.reset_session()

    # Start FastAPI in background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Wait for server to be ready
    time.sleep(1.5)

    # Open native desktop window
    webview.create_window(
        title="💰 Save Token",
        url="http://127.0.0.1:8000",
        width=1200,
        height=800,
        min_size=(800, 600),
        resizable=True,
    )
    webview.start()
