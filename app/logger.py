"""
logger.py — Session log handler for Save Token.

One file per session. Logs both compress and expand operations in sequence.
File named: logs/YYYY-MM-DD/YYYY-MM-DD_HH-MM.txt
Session starts on first operation after app launch.
Session ends when the window/process is closed.
"""

import os
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LOGS_DIR = REPO_ROOT / "logs"

SESSION_GAP_SECONDS = 30 * 60  # 30 minutes idle = new session

_current_log_path: Path | None = None
_last_log_time: datetime | None = None
_session_start_time: datetime | None = None


def _now() -> datetime:
    return datetime.now()


def _make_log_path(dt: datetime) -> Path:
    date_folder = dt.strftime("%Y-%m-%d")
    filename = dt.strftime("%Y-%m-%d_%H-%M") + ".txt"
    return LOGS_DIR / date_folder / filename


def _ensure_session() -> Path:
    global _current_log_path, _last_log_time, _session_start_time

    now = _now()

    if _current_log_path is None or _last_log_time is None:
        _current_log_path = _make_log_path(now)
        _session_start_time = now
        _current_log_path.parent.mkdir(parents=True, exist_ok=True)
        # Write session header
        with open(_current_log_path, "a", encoding="utf-8") as f:
            f.write(f"{'='*56}\n")
            f.write(f"  Save Token Session — {now.strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{'='*56}\n\n")
    else:
        gap = (now - _last_log_time).total_seconds()
        if gap > SESSION_GAP_SECONDS:
            _current_log_path = _make_log_path(now)
            _session_start_time = now
            _current_log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(_current_log_path, "a", encoding="utf-8") as f:
                f.write(f"{'='*56}\n")
                f.write(f"  Save Token Session — {now.strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"{'='*56}\n\n")

    return _current_log_path


def log_compress(original: str, compressed: str, model_used: str, words_saved: int, percent_saved: int) -> None:
    """Log a compression operation."""
    global _last_log_time

    log_path = _ensure_session()
    now = _now()
    _last_log_time = now

    timestamp = now.strftime("%H:%M:%S")
    sep = "-" * 48

    entry = (
        f"\n[{timestamp}] COMPRESS  ({words_saved} words saved, {percent_saved}% reduction)\n"
        f"Model: {model_used}\n"
        f"{sep}\n"
        f"ORIGINAL:\n{original.strip()}\n"
        f"{sep}\n"
        f"COMPRESSED:\n{compressed.strip()}\n"
        f"{sep}\n"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def log_expand(compressed_input: str, expanded: str, model_used: str) -> None:
    """Log an expansion operation."""
    global _last_log_time

    log_path = _ensure_session()
    now = _now()
    _last_log_time = now

    timestamp = now.strftime("%H:%M:%S")
    sep = "-" * 48

    entry = (
        f"\n[{timestamp}] EXPAND\n"
        f"Model: {model_used}\n"
        f"{sep}\n"
        f"COMPRESSED INPUT:\n{compressed_input.strip()}\n"
        f"{sep}\n"
        f"EXPANDED OUTPUT:\n{expanded.strip()}\n"
        f"{sep}\n"
    )

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def get_log_path() -> str:
    if _current_log_path is None:
        return "No log file yet"
    return str(_current_log_path)


def get_logs_dir() -> str:
    return str(LOGS_DIR)


def reset_session() -> None:
    """Force-start a new log session (called on app startup)."""
    global _current_log_path, _last_log_time, _session_start_time
    _current_log_path = None
    _last_log_time = None
    _session_start_time = None
