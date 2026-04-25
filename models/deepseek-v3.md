# DeepSeek V3 — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with DeepSeek V3. It tells the local model how to shape your compressed text to get the best results from DeepSeek V3 specifically.

---

## About DeepSeek V3

DeepSeek V3 is DeepSeek's latest general-purpose chat model. Extremely capable for coding and technical tasks. One of the best-value models available — very competitive with much more expensive models. Available via DeepSeek's API.

**Token cost**: Very low. DeepSeek is significantly cheaper than equivalent OpenAI/Anthropic models. Still worth compressing — savings add up at volume.

**Strengths**: Excellent coding ability, strong at technical and scientific questions, good instruction following.

---

## Compression Hints for DeepSeek V3

When compressing text for DeepSeek V3, the local model should:

- Use `full` mode — DeepSeek V3 handles terse technical input very well
- DeepSeek excels at code: compressed code questions work extremely well
- Include language/framework context: "Python", "TypeScript", "SQL", "Rust"
- Use `ultra` mode for simple factual or coding questions — DeepSeek handles very compressed input
- For complex tasks, include expected output format: "Function signature:", "Step-by-step:", "Algorithm only:"

---

## Example Compressions

**Original** (31 words): "I want to implement a binary search algorithm in Python. Can you show me the code and explain how it works and what its time complexity is?"

**Compressed for DeepSeek V3** (14 words): "Python binary search: implementation + explanation + time complexity. Code first, then explain."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
