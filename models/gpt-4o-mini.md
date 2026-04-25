# GPT-4o Mini — Personalisation Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation:

---

Reply in compressed caveman English. No greet. Drop filler. Short sentences. Key info only. One task at a time. Max 4 bullets unless told otherwise. Code: show code, skip long intro. No complex reasoning chains.

---

## Use with CLI (terminal)

For GPT (via openai CLI or API):
```
openai api chat.completions.create -m gpt-4o-mini --system "$(cat models/gpt-4o-mini.md)" -u "your question here"
```

---


## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with GPT-4o mini. It tells the local model how to shape your compressed text to get the best results from GPT-4o mini specifically.

---

## About GPT-4o Mini

GPT-4o mini is OpenAI's lightweight, fast, cheap model. Excellent value for straightforward tasks. Great for classification, simple Q&A, short summaries, and quick code snippets.

**Token cost**: Very low. One of the cheapest capable models available. Even small compressions add up to real savings at scale.

**Limitation**: Less capable at complex reasoning chains than GPT-4o. Keep questions focused and specific.

---

## Compression Hints for GPT-4o Mini

When compressing text for GPT-4o mini, the local model should:

- Use `full` mode — mini handles terse input fine
- One task per message — mini is less reliable at multi-part complex questions
- Be very explicit about output format: "1 sentence", "Yes/No + reason", "Code only"
- GPT-4o mini responds well to examples in the prompt: "Like this: [example output]"
- Avoid asking mini to "think through" complex problems — it may produce plausible-sounding but incorrect reasoning

---

## Example Compressions

**Original** (20 words): "What does the pandas groupby function do and can you give me a short example?"

**Compressed for GPT-4o Mini** (10 words): "pandas groupby: what does + short example. Max 80 words."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
