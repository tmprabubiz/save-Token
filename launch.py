"""
launch.py — Launch Save Token as a standalone desktop window.

Usage:
  python launch.py

Opens the app as a native window in the Windows taskbar (not a browser tab).
The window minimises to the taskbar. Closing the window ends the session and
finalises the log file.
"""

import threading
import time
import sys
from pathlib import Path

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
    session_logger.reset_session()

    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1.5)

    webview.create_window(
        title="💰 Save Token",
        url="http://127.0.0.1:8000",
        width=1280,
        height=900,
        min_size=(800, 600),
        resizable=True,
    )
    webview.start()
