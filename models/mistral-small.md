# Mistral Small — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Mistral Small. It tells the local model how to shape your compressed text to get the best results from Mistral Small specifically.

---

## About Mistral Small

Mistral Small is Mistral AI's fast, lightweight model. Very cheap to run at high volume. Good at classification, simple Q&A, translation, and short content tasks. Less capable than Mistral Large for complex reasoning.

**Token cost**: Very low. One of the cheapest capable API models. Even small compressions are worth making at scale.

**Best for**: Quick lookups, simple coding questions, translation, classification, summarising short texts.

---

## Compression Hints for Mistral Small

When compressing text for Mistral Small, the local model should:

- Use `full` mode
- Keep tasks simple and single-focus — Mistral Small is less reliable for multi-step tasks
- Always specify the exact output format: "1 sentence", "Yes or No + reason", "JSON only"
- For translation tasks: "Translate to [language]:" followed by the text
- Avoid abstract reasoning tasks — use Mistral Large for those

---

## Example Compressions

**Original** (18 words): "Can you translate the following sentence into French and tell me if it sounds natural?"

**Compressed for Mistral Small** (9 words): "Translate to French. Note if natural: [sentence here]"

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
