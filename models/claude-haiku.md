# Claude Haiku — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Claude Haiku. It tells the local model how to shape your compressed text to get the best results from Claude Haiku specifically.

---

## About Claude Haiku

Claude Haiku is Anthropic's fastest and cheapest Claude model. It is designed for high-volume, low-latency tasks. Excellent for simple questions, quick lookups, short summaries, and tasks where speed matters more than depth.

**Token cost**: Very low. The cheapest Claude option. Best for quick iterative questions.

**Limitation**: Less capable at complex multi-step reasoning than Sonnet or Opus. Keep tasks simple and focused.

---

## ⚠️ Tone Warning — Read This First

Claude gives dramatically longer responses when you are casual, friendly, or use filler phrases.

Haiku is fast, but if you are chatty, it will still generate a long response — and that costs you tokens. More importantly, Haiku can produce lower-quality long responses than Sonnet. You want Haiku short and sharp.

**Write to Claude like you are sending a formal note, not a WhatsApp message.**

Bad: "Hi! Quick question — what's the difference between a list and a tuple in Python? Thanks!"

Good: "Python: list vs tuple. Key differences only. Max 4 bullet points."

---

## Compression Hints for Claude Haiku

When compressing text for Claude Haiku, the local model should:

- Use `full` mode — Haiku handles terse input well and rewards it with focused answers
- Keep tasks to **one thing at a time** — Haiku is less reliable at multi-part questions
- Always specify output length: "1 sentence", "3 bullets", "one-line answer"
- Avoid asking Haiku to "think through" or "reason about" complex topics — use Sonnet for that
- Great use cases in compressed form: "Define X", "Syntax for Y in Z", "Fix this error:", "Translate this to"

---

## Example Compressions

**Original** (25 words): "What is the difference between GET and POST requests in HTTP? Can you give me a quick explanation?"

**Compressed for Claude Haiku** (11 words): "HTTP GET vs POST: differences. 3 bullet points max."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*

Example: "Marketing professional, using AI for content drafting."
Example: "Student, asking quick factual questions for study notes."
