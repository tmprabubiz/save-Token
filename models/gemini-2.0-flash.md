# Gemini 2.0 Flash — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Gemini 2.0 Flash. It tells the local model how to shape your compressed text to get the best results from Gemini 2.0 Flash specifically.

---

## About Gemini 2.0 Flash

Gemini 2.0 Flash is Google's fast, efficient model. Designed for speed and low cost. Has a very generous free tier — one of the best free options for high-volume use. Good at code, factual Q&A, and summarisation.

**Token cost**: Very low. The free tier is generous — check current limits at ai.google.dev. Even at paid rates, Flash is cheap.

**Free tier**: Available through Google AI Studio and the Gemini API. Check current limits yourself — they change. Search "Gemini 2.0 Flash free tier limits" for the latest.

---

## Compression Hints for Gemini 2.0 Flash

When compressing text for Gemini 2.0 Flash, the local model should:

- Use `full` mode — Flash handles terse input well
- Flash is good at structured output: "JSON:", "Table:", "Numbered steps:"
- Gemini models respond well to explicit task framing: "Classify:", "Summarise:", "Generate:"
- Include constraints: "Max 100 words", "3 items only", "No code, explanation only"
- Flash is less strong at long chains of reasoning — break complex questions into steps

---

## Example Compressions

**Original** (24 words): "Can you classify this customer review as positive, negative or neutral and explain your reasoning briefly?"

**Compressed for Gemini 2.0 Flash** (12 words): "Classify review: positive/negative/neutral. 1-sentence reason. Review: [paste here]"

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
