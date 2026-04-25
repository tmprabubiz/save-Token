# Mistral Large — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Mistral Large. It tells the local model how to shape your compressed text to get the best results from Mistral Large specifically.

---

## About Mistral Large

Mistral Large is Mistral AI's flagship model. Strong at reasoning, coding, and multilingual tasks. Generally more concise in its responses than Claude or GPT-4 — Mistral tends not to over-explain unless asked. Good value for the capability level.

**Token cost**: Medium. Available via Mistral's API (api.mistral.ai). Check current pricing at mistral.ai.

**Strengths**: Efficient, direct responses. Strong at European languages. Good at code. Follows instructions well.

---

## Compression Hints for Mistral Large

When compressing text for Mistral Large, the local model should:

- Use `full` mode — Mistral handles terse input well
- Mistral is naturally concise, so you do not need to specify "be brief" explicitly
- For code tasks, Mistral understands compressed code context well
- Include language context if relevant: "French:", "German:", for multilingual tasks
- Mistral follows structured prompts well: "Task:", "Context:", "Expected output:"

---

## Example Compressions

**Original** (27 words): "I need to write a regular expression in Python that matches email addresses but also handles edge cases like subdomains and special characters."

**Compressed for Mistral Large** (13 words): "Python regex: match email addresses incl. subdomains, special chars. Provide pattern + explanation."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
