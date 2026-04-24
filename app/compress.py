"""
compress.py — Compress verbose text into token-efficient caveman style.

Reads SKILL.md for compression rules and sends to the local model.
"""

import re
from pathlib import Path

# Path to the SKILL.md file
REPO_ROOT = Path(__file__).parent.parent
SKILL_PATH = REPO_ROOT / "models" / "SKILL.md"


def load_skill_md() -> str:
    """Load the SKILL.md content for use as system prompt context."""
    if SKILL_PATH.exists():
        return SKILL_PATH.read_text(encoding="utf-8")
    return ""


def build_compress_prompt(text: str, mode: str, personalisation: str = "") -> str:
    """
    Build the prompt for the compression model.

    Args:
        text: The verbose text to compress
        mode: one of lite / full / ultra / wenyan-lite / wenyan-full / wenyan-ultra
        personalisation: optional user background/context
    """
    skill_content = load_skill_md()

    persona_block = ""
    if personalisation and personalisation.strip():
        persona_block = f"\n## User Context\n{personalisation.strip()}\n"

    prompt = f"""You are a token compression assistant. Your job is to compress the user's text into efficient shorthand following the rules below.

{skill_content}
{persona_block}
## Instructions

Compress the following text using **{mode}** compression level.

Rules:
- Output ONLY the compressed text. No explanation, no preamble, no "Here is the compressed version:".
- Do not add quotes around the output.
- Preserve all technical terms, error messages, file names, URLs, and code exactly.
- Never remove negations (not, no, never, can't, won't, without).
- Code inside backticks is copied verbatim, never compressed.

## Text to compress:

{text.strip()}

## Compressed output:"""

    return prompt


def build_compress_messages(text: str, mode: str, personalisation: str = "") -> list[dict]:
    """
    Build the messages array for the chat API call.
    """
    skill_content = load_skill_md()

    persona_block = ""
    if personalisation and personalisation.strip():
        persona_block = f"\n\nUser context: {personalisation.strip()}"

    system_message = f"""You are a token compression assistant. You compress verbose English into efficient shorthand.

Follow these compression rules exactly:
{skill_content}
{persona_block}

Output ONLY the compressed text. No explanation, no preamble. Just the compressed result."""

    user_message = f"""Compress this text using {mode} compression level:

{text.strip()}"""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split()) if text.strip() else 0


def calculate_savings(original: str, compressed: str) -> dict:
    """
    Calculate token/word savings between original and compressed text.
    Returns word counts and percentage saved.
    """
    orig_words = count_words(original)
    comp_words = count_words(compressed)
    saved = orig_words - comp_words
    pct = round((saved / orig_words * 100) if orig_words > 0 else 0)
    return {
        "original_words": orig_words,
        "compressed_words": comp_words,
        "words_saved": saved,
        "percent_saved": pct,
    }
