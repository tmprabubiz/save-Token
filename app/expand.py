"""
expand.py — Expand caveman-style compressed text back to clear English.

Takes compressed text from a MODEL response and expands it to readable English.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILL_PATH = REPO_ROOT / "models" / "SKILL.md"


def load_skill_md() -> str:
    """Load the SKILL.md content."""
    if SKILL_PATH.exists():
        return SKILL_PATH.read_text(encoding="utf-8")
    return ""


def build_expand_messages(compressed_text: str) -> list[dict]:
    """
    Build the messages array for expanding caveman text to readable English.
    """
    skill_content = load_skill_md()

    system_message = f"""You are a text expansion assistant. You convert compressed caveman-style shorthand back into clear, readable English.

The compression rules that were used:
{skill_content}

Your expansion rules:
1. Reconstruct full sentences with proper grammar and punctuation.
2. Add articles (a, an, the) where natural.
3. Expand abbreviations to full words.
4. Add connecting words to make sentences flow naturally.
5. Keep ALL technical terms exactly as written — never paraphrase error messages, code, file names, or library names.
6. Match the technical depth of the input — if it was a complex technical question, give a clear technical answer.
7. Do not add opinions, warnings, or extra information not implied by the original.
8. Aim for clarity, not verbosity — expanded text should be readable but not padded.

Output ONLY the expanded text. No explanation, no preamble."""

    user_message = f"""Expand this compressed text back to clear, readable English:

{compressed_text.strip()}"""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
