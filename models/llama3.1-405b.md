# Llama 3.1 405B — Personalisation Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation:

---

Reply in compressed caveman English. No greet. Drop filler. Short sentences. Key info only. Structured prompts: follow Task/Context/Output format. Expert personas ok. Format as given. Constraints: respect word limits.

---

## Use with CLI (terminal)

For Llama via Groq (free tier available):
```
curl -s -X POST "https://api.groq.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"llama-3.1-405b-reasoning\",\"messages\":[{\"role\":\"system\",\"content\":\"$(cat models/llama3.1-405b.md)\"},{\"role\":\"user\",\"content\":\"your question here\"}]}"
```

---


## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Llama 3.1 405B. It tells the local model how to shape your compressed text to get the best results from Llama 3.1 405B specifically.

---

## About Llama 3.1 405B

Llama 3.1 405B is Meta's largest open-source language model. It is one of the most capable open-source models available. You cannot run it locally unless you have an enormous amount of VRAM (multiple high-end GPUs). Instead, you access it through API services like Groq or Together AI.

**Token cost**: Low via Groq (free tier available — check current limits at console.groq.com). Moderate via Together AI. Much cheaper than equivalent proprietary models.

**Free tier note**: Groq offers a free tier for Llama models. Check current rate limits at console.groq.com — limits change. Search "Groq free tier limits" for the latest information. Do not rely on any specific numbers in this document as they change frequently.

**Strengths**: Excellent general capability, good at reasoning, strong code generation. Very good instruction following for an open-source model.

---

## Compression Hints for Llama 3.1 405B

When compressing text for Llama 3.1 405B, the local model should:

- Use `full` mode — Llama 3.1 405B handles terse input well
- Llama follows structured prompts well: "Task:", "Context:", "Output:"
- Include format instructions explicitly: "Numbered list:", "Code block:", "Table:"
- Llama is good at role-playing expert personas: "As data engineer:", "As security expert:"
- Include constraints: "Max 200 words", "Python only", "No explanations, code only"

---

## Accessing via Groq

1. Go to console.groq.com and create a free account
2. Get your API key from the API Keys section
3. Use the API key in your preferred AI chat client or the Groq playground
4. Select `llama-3.1-405b-reasoning` or `llama3-70b-8192` (check available models — they change)

---

## Example Compressions

**Original** (30 words): "I need to understand how transformer attention mechanisms work. Can you explain it in a way that someone with basic ML knowledge would understand?"

**Compressed for Llama 3.1 405B** (14 words): "Transformer attention mechanism: explain for ML beginner. Analogy + diagram description. Max 250 words."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
