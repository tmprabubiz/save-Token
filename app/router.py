"""
router.py — Route between chat model and coding model based on content signals.

Rules:
- Count code-related keywords in the text
- 2 or more signals → coding model (qwen2.5-coder:7b)
- Fewer than 2 → chat model (gemma3:12b)
- Falls back to whichever model is actually available
"""

# Code signal keywords
CODE_SIGNALS = [
    "def ",
    "class ",
    "function",
    "import ",
    "error:",
    "traceback",
    "exception",
    " fix ",
    " bug ",
    "sql",
    ".py",
    ".js",
    ".ts",
    ".go",
    ".rs",
    "```",
    "git ",
    "docker",
    "bash",
    "regex",
    " api",
    "http",
    "localhost",
    "npm ",
    "pip ",
    "poetry",
    "pytest",
    "unittest",
]

# Preferred models in priority order
PREFERRED_CHAT_MODELS = ["gemma3:12b", "gemma3", "phi3:mini", "phi3", "tinyllama:1.1b", "tinyllama"]
PREFERRED_CODE_MODELS = ["qwen2.5-coder:7b", "qwen2.5-coder", "deepseek-coder:1.3b", "deepseek-coder", "starcoder2:3b", "starcoder2"]

# Threshold for switching to code model
CODE_SIGNAL_THRESHOLD = 2


def count_code_signals(text: str) -> int:
    """Count how many code-related signals appear in the text."""
    text_lower = text.lower()
    count = 0
    for signal in CODE_SIGNALS:
        if signal.lower() in text_lower:
            count += 1
    return count


def pick_model(text: str, available_models: list[str]) -> tuple[str, str, str]:
    """
    Choose the best model for the given text from available models.

    Returns:
        (model_name, route_type, reason)
        route_type: "chat" or "code"
        reason: human-readable explanation
    """
    from app.model_detect import pick_best_model

    signal_count = count_code_signals(text)

    if signal_count >= CODE_SIGNAL_THRESHOLD:
        route = "code"
        # Try code model first
        model = pick_best_model(available_models, PREFERRED_CODE_MODELS)
        if model:
            return model, route, f"code signals detected ({signal_count}) → code model"
        # Fall back to chat model
        model = pick_best_model(available_models, PREFERRED_CHAT_MODELS)
        if model:
            return model, route, f"code signals detected but code model unavailable → chat model fallback"
    else:
        route = "chat"
        model = pick_best_model(available_models, PREFERRED_CHAT_MODELS)
        if model:
            return model, route, f"general question → chat model"
        # Fall back to any available model
        model = pick_best_model(available_models, PREFERRED_CODE_MODELS)
        if model:
            return model, route, f"chat model unavailable → code model fallback"

    # If no preferred model found, use whatever is available
    if available_models:
        model = available_models[0]
        return model, route, f"no preferred model available → using {model}"

    raise RuntimeError(
        "No models are available. "
        "Please download a model first. "
        "Run: ollama pull gemma3:12b"
    )
