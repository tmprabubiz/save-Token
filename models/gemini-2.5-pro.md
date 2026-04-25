# Gemini 2.5 Pro — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Gemini 2.5 Pro. It tells the local model how to shape your compressed text to get the best results from Gemini 2.5 Pro specifically.

---

## About Gemini 2.5 Pro

Gemini 2.5 Pro is Google's most capable Gemini model. Excellent at complex reasoning, coding, long-context tasks (up to 1 million tokens), and research synthesis. The reasoning-capable version is particularly good at step-by-step problem solving.

**Token cost**: Medium-high for paid use. Check current pricing at ai.google.dev. Has a limited free tier via Google AI Studio — check current limits yourself.

**Strengths**: Extremely long context, complex reasoning, code generation, multi-document analysis.

---

## Compression Hints for Gemini 2.5 Pro

When compressing text for Gemini 2.5 Pro, the local model should:

- Use `full` or `ultra` mode — Gemini 2.5 Pro handles very terse input excellently
- Specify reasoning depth: "Step-by-step reasoning:", "Quick answer:", "Deep analysis:"
- For long-context tasks: compress the question, not the document — Gemini's strength is handling the long document
- Include explicit output structure: "Format: Problem / Root cause / Solution / Prevention"
- Gemini 2.5 Pro is good at self-correction: "If unsure, say so." works well

---

## Example Compressions

**Original** (44 words): "I'm trying to understand the performance implications of using different indexing strategies in PostgreSQL. I have a large table with millions of rows and queries are getting slow. What should I look at and in what order?"

**Compressed for Gemini 2.5 Pro** (18 words): "PostgreSQL perf: large table, slow queries. Index strategies — what to check, priority order. Context: millions rows."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
