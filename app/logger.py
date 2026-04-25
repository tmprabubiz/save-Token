"""
logger.py — Session log handler for Save Token.

Logs expanded (readable English) content only — never raw caveman text.
One file per session. New file when app starts OR when gap > 30 minutes.
File naming: logs/MMDDYYYY/MMDDYYYY_HHMMSS.txt (Windows-safe, no colons).
"""

import os
import re
from datetime import datetime, timezone
from pathlib import Path

# Repo root is one level up from this file
REPO_ROOT = Path(__file__).parent.parent
LOGS_DIR = REPO_ROOT / "logs"

# New session if gap between entries exceeds this many seconds
SESSION_GAP_SECONDS = 30 * 60  # 30 minutes

_current_log_path: Path | None = None
_last_log_time: datetime | None = None


def _now() -> datetime:
    return datetime.now()


def _make_log_path(dt: datetime) -> Path:
    """
    Build log path: logs/MMDDYYYY/MMDDYYYY_HHMMSS.txt
    """
    date_folder = dt.strftime("%m%d%Y")
    filename = dt.strftime("%m%d%Y_%H%M%S") + ".txt"
    return LOGS_DIR / date_folder / filename


def _ensure_new_session() -> Path:
    """
    Decide whether to start a new log file.
    Start new session if:
    - No current log file exists, or
    - Gap since last entry exceeds SESSION_GAP_SECONDS
    """
    global _current_log_path, _last_log_time

    now = _now()

    if _current_log_path is None or _last_log_time is None:
        _current_log_path = _make_log_path(now)
    else:
        gap = (now - _last_log_time).total_seconds()
        if gap > SESSION_GAP_SECONDS:
            _current_log_path = _make_log_path(now)

    _current_log_path.parent.mkdir(parents=True, exist_ok=True)
    return _current_log_path


def log_entry(
    original_compressed: str,
    expanded: str,
    model_used: str,
    route: str,
    mode: str,
) -> None:
    """
    Append a log entry to the current session file.

    Format:
    ----------------------------------------
    [04/24/2026 14:32:01]
    Model: gemma3:12b | Route: chat | Mode: full
    Compressed input: <compressed text>
    Expanded output:
    <expanded readable English>
    ----------------------------------------
    """
    global _last_log_time

    log_path = _ensure_new_session()
    now = _now()
    _last_log_time = now

    timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
    separator = "-" * 48

    entry = (
        f"\n{separator}\n"
        f"[{timestamp}]\n"
        f"Model: {model_used} | Route: {route} | Mode: {mode}\n"
        f"Compressed input: {original_compressed.strip()}\n"
        f"Expanded output:\n{expanded.strip()}\n"
        f"{separator}\n"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def get_log_path() -> str:
    """Return the current log file path as a string (for status display)."""
    if _current_log_path is None:
        return "No log file yet"
    return str(_current_log_path)


def reset_session() -> None:
    """Force-start a new log session (called on app startup)."""
    global _current_log_path, _last_log_time
    _current_log_path = None
    _last_log_time = None
