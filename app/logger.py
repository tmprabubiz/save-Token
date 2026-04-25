"""
logger.py — Session log handler for Save Token.

One file per session. Logs BOTH compress and expand operations in sequence.
File: logs/YYYY-MM-DD/YYYY-MM-DD_HH-MM.txt
Session starts on first operation. New session after 30 min idle or on reset.
Closing the window/process finalises the file automatically (OS flush on exit).
"""

import os
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LOGS_DIR = REPO_ROOT / "logs"
SESSION_GAP_SECONDS = 30 * 60

_current_log_path: Path | None = None
_last_log_time: datetime | None = None


def _now() -> datetime:
    return datetime.now()


def _make_log_path(dt: datetime) -> Path:
    date_folder = dt.strftime("%Y-%m-%d")
    filename = dt.strftime("%Y-%m-%d_%H-%M") + ".txt"
    return LOGS_DIR / date_folder / filename


def _ensure_session() -> Path:
    global _current_log_path, _last_log_time
    now = _now()
    if _current_log_path is None or _last_log_time is None:
        _current_log_path = _make_log_path(now)
        _current_log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(_current_log_path, "a", encoding="utf-8") as f:
            f.write(f"{'='*56}\n")
            f.write(f"  \U0001f4b0 Save Token Session — {now.strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{'='*56}\n\n")
    else:
        gap = (now - _last_log_time).total_seconds()
        if gap > SESSION_GAP_SECONDS:
            _current_log_path = _make_log_path(now)
            _current_log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(_current_log_path, "a", encoding="utf-8") as f:
                f.write(f"{'='*56}\n")
                f.write(f"  \U0001f4b0 Save Token Session — {now.strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"{'='*56}\n\n")
    return _current_log_path


def log_compress(original: str, compressed: str, model_used: str, words_saved: int, percent_saved: int) -> None:
    global _last_log_time
    log_path = _ensure_session()
    now = _now()
    _last_log_time = now
    sep = "-" * 48
    entry = (
        f"\n[{now.strftime('%H:%M:%S')}] COMPRESS  \u2014  {words_saved} words saved ({percent_saved}% smaller)\n"
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
    global _last_log_time
    log_path = _ensure_session()
    now = _now()
    _last_log_time = now
    sep = "-" * 48
    entry = (
        f"\n[{now.strftime('%H:%M:%S')}] EXPAND\n"
        f"Model: {model_used}\n"
        f"{sep}\n"
        f"COMPRESSED INPUT:\n{compressed_input.strip()}\n"
        f"{sep}\n"
        f"EXPANDED OUTPUT:\n{expanded.strip()}\n"
        f"{sep}\n"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


# Keep old name as alias so existing calls don't break
def log_entry(original_compressed: str, expanded: str, model_used: str, route: str = "", mode: str = "") -> None:
    log_expand(original_compressed, expanded, model_used)


def get_log_path() -> str:
    return str(_current_log_path) if _current_log_path else "No log file yet"


def get_logs_dir() -> str:
    return str(LOGS_DIR)


def reset_session() -> None:
    global _current_log_path, _last_log_time
    _current_log_path = None
    _last_log_time = None
