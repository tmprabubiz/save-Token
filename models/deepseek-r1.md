# DeepSeek R1 — Personalisation Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation:

---

You are a reasoning model. Reason fully then give concise final answer. No greet. Give all constraints/facts in input — rely on them for reasoning. If only final answer needed, user will say "Final answer only". Code: include error messages verbatim.

---

## Use with CLI (terminal)

For DeepSeek (via API):
```
curl -s -X POST "https://api.deepseek.com/chat/completions" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"deepseek-reasoner\",\"system\":\"$(cat models/deepseek-r1.md)\",\"messages\":[{\"role\":\"user\",\"content\":\"your question here\"}]}"
```

---


## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with DeepSeek R1. It tells the local model how to shape your compressed text to get the best results from DeepSeek R1 specifically.

---

## About DeepSeek R1

DeepSeek R1 is DeepSeek's reasoning model — similar to OpenAI's o1 series. It thinks step-by-step before answering. Excellent at complex mathematical, scientific, and logical reasoning problems. It will show its work (chain of thought) unless you ask it not to.

**Token cost**: Higher than V3 due to the reasoning chain. The thinking process uses tokens. However, the quality of answers for hard problems makes it worthwhile. Compression helps reduce input tokens.

**Best for**: Complex maths, logic puzzles, scientific reasoning, debugging complex code, multi-step planning.

**Note**: R1 generates a reasoning chain before its answer. This is visible and cannot be fully suppressed. It is a feature, not a bug — the reasoning chain shows you exactly how the model solved the problem.

---

## Compression Hints for DeepSeek R1

When compressing text for DeepSeek R1, the local model should:

- Use `full` mode — R1 handles terse input well
- For reasoning tasks: provide all constraints and known facts in compressed form — R1 will reason from them
- Do NOT ask R1 to "be brief" — it will reason fully and give a complete answer. That is what you are paying for.
- Include all relevant numbers, variables, and conditions — R1's reasoning depends on precise inputs
- For coding debugging: include the error message and relevant code verbatim (in backticks — they are never compressed)
- If you only want the final answer: add "Final answer only, skip reasoning." at the end of compressed text

---

## Example Compressions

**Original** (35 words): "I have a recursive function that keeps hitting Python's recursion limit. The function calculates Fibonacci numbers and it starts failing when I try numbers above about 900. How can I fix this?"

**Compressed for DeepSeek R1** (17 words): "Python recursion limit: Fibonacci fn fails >900. Fix options: memoization, iteration, sys.setrecursionlimit. Recommend best approach."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*
