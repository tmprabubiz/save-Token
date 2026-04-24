# GPT-4o — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with GPT-4o. It tells the local model how to shape your compressed text to get the best results from GPT-4o specifically.

---

## About GPT-4o

GPT-4o ("omni") is OpenAI's flagship multimodal model. It handles text, images, audio, and code. Fast, capable, and reasonably priced. Excellent at following structured instructions and producing formatted output.

**Token cost**: Medium. More expensive than GPT-4o mini, cheaper than earlier GPT-4 variants. Compression gives meaningful savings.

**Strengths**: Code generation, structured output, following explicit formatting instructions, multi-modal tasks.

---

## Compression Hints for GPT-4o

When compressing text for GPT-4o, the local model should:

- Use `full` mode — GPT-4o handles terse input reliably
- GPT-4o follows format instructions very well: "Return JSON:", "Markdown table:", "Numbered list:"
- Include persona framing for technical tasks: "As Python expert:", "As code reviewer:"
- Specify tone when needed: "Formal.", "Plain English.", "Technical detail."
- GPT-4o is good at constrained output: "Max 5 steps", "One-line summary only", "Code only, no explanation"
- Remove all hedging and social filler — GPT-4o does not need encouragement

---

## Example Compressions

**Original** (33 words): "Can you help me write a Python function that reads a CSV file and returns only the rows where the sales column is greater than 1000?"

**Compressed for GPT-4o** (16 words): "Python fn: read CSV, filter rows where sales > 1000. Return filtered rows."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*

Example: "Full-stack developer using GPT-4o for code generation and review."
Example: "Content creator using GPT-4o for writing and editing."
