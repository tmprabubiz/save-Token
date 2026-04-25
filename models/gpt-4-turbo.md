# GPT-4 Turbo — Personalisation Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation:

---

Reply in compressed caveman English. No greet. Drop filler. Short sentences. Key info only. Follow format instructions exactly (Task/Context/Output). Long docs: process efficiently, no recap. No social preamble.

---

## Use with CLI (terminal)

For GPT (via openai CLI or API):
```
openai api chat.completions.create -m gpt-4-turbo --system "$(cat models/gpt-4-turbo.md)" -u "your question here"
```

---


## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with GPT-4 Turbo. It tells the local model how to shape your compressed text to get the best results from GPT-4 Turbo specifically.

---

## About GPT-4 Turbo

GPT-4 Turbo is an earlier OpenAI flagship model with a 128K context window. Highly capable and reliable. Generally superseded by GPT-4o for new work, but still available and used in many existing integrations.

**Token cost**: Medium-high. More expensive than GPT-4o on a per-token basis. Compression gives meaningful savings, especially with long context.

**Strengths**: Long document processing, complex instructions, reliable structured output.

---

## Compression Hints for GPT-4 Turbo

When compressing text for GPT-4 Turbo, the local model should:

- Use `full` mode — GPT-4 Turbo handles terse input well
- Particularly useful for long-context tasks: compress the question, not the document being analysed
- Include explicit section markers for structured tasks: "Task:", "Context:", "Output format:"
- GPT-4 Turbo follows system-style instructions well in compressed form
- Remove all social preamble — it does not affect the model positively

---

## Example Compressions

**Original** (29 words): "I have a long document about company policies and I need to extract all the dates mentioned and create a timeline. How should I approach this?"

**Compressed for GPT-4 Turbo** (14 words): "Task: extract all dates from policy document → chronological timeline. Approach?"

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
