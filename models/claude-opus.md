# Claude Opus — Personalisation Guide

## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Claude Opus. It tells the local model how to shape your compressed text to get the best results from Claude Opus specifically.

---

## About Claude Opus

Claude Opus is Anthropic's most powerful Claude model. It has the deepest reasoning, longest context, and best performance on complex multi-step tasks. It is also the most expensive Claude model.

**Token cost**: High. Opus is significantly more expensive than Sonnet and orders of magnitude more expensive than Haiku. Token savings matter most here — compressing before sending to Opus has the largest financial impact of any Claude model.

**When to use**: Complex reasoning, long document analysis, creative writing with many constraints, multi-step problem solving, tasks where quality matters more than cost.

---

## ⚠️ Tone Warning — CRITICAL for Opus

Claude gives dramatically longer responses when you are casual, friendly, or use filler phrases. **This effect is strongest with Opus.**

Opus is so capable that if you give it an informal question, it will write you a textbook chapter. An offhand "how does X work?" can produce 2,000 words. That is not always what you want, and it is expensive.

**Write to Claude Opus like you are briefing a senior consultant. Formal, specific, and bounded.**

Bad: "Hey Opus, I've been thinking about building a SaaS product and I'd love your thoughts on the best architecture approach. Maybe with some examples? Thanks so much!"

Good: "SaaS architecture: monolith vs microservices. My context: solo dev, 500 users target, Python/FastAPI stack. Recommend one approach + rationale. Max 300 words."

Every social phrase you add ("I'd love your thoughts", "thanks so much", "no rush") causes Opus to mirror that warm, expansive register — and Opus in that register is extremely verbose.

---

## Compression Hints for Claude Opus

When compressing text for Claude Opus, the local model should:

- Use `full` or `ultra` mode — Opus handles very terse input excellently
- **Always include output constraints**: word count, format, section headings expected
- Include your context and constraints explicitly — Opus uses them to self-limit
- State what you already know to skip basics: "Familiar with Docker basics. Skip intro."
- Use structural directives: "Structure as: Problem → Solution → Trade-offs"
- Opus is excellent at role-playing expert personas even in compressed form: "As security auditor:"

---

## Example Compressions

**Original** (52 words): "I'm building a web application and I need to understand the best way to handle user authentication. I'm using Python and FastAPI. I want to know about JWT tokens and session-based auth and when to use which one. I'm not sure about the security implications either."

**Compressed for Claude Opus** (20 words): "FastAPI auth: JWT vs session-based. Context: web app, Python. Security implications. Recommend one + when to switch. Max 250 words."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*

Example: "Senior developer using Opus for architectural decisions."
Example: "Researcher using Opus for literature analysis and synthesis."
