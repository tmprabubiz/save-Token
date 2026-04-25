# Claude Sonnet — Personalisation Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation:

---

Reply in compressed caveman English. No greet. Drop filler. Short sentences. Key info only. If user ask question, answer direct. No explain obvious. Use bullets when list. Code: show code, skip long intro. Technical terms ok, no fluff around them.

---

## Use with CLI (terminal)

For Claude CLI:
```
claude --system-file models/claude-sonnet.md "your question here"
```

---


## What This File Is For

Paste the contents of this file into the personalisation bar in Save Token before you start a session with Claude Sonnet. It tells the local model how to shape your compressed text to get the best results from Claude Sonnet specifically.

You can edit the personalisation bar text — it is a suggestion, not a locked setting.

---

## About Claude Sonnet

Claude Sonnet is Anthropic's mid-tier model — faster than Opus, more capable than Haiku. It is very good at following instructions and giving structured answers. It tends toward thorough, detailed responses.

**Token cost**: Medium. Significantly cheaper than Opus. Responds well to compression.

---

## ⚠️ Tone Warning — Read This First

Claude gives dramatically longer responses when you are casual, friendly, or use filler phrases.

Every "please", "thanks", "hope you're doing well", "could you maybe", "I was just wondering" costs you tokens — not just in your message, but in Claude's response too. Claude mirrors your tone. If you are relaxed and chatty, Claude writes you a relaxed, chatty essay.

**Write to Claude like you are sending a formal note, not a WhatsApp message.**

Bad: "Hey Claude! Could you maybe help me understand how Python decorators work? I've been struggling with them for a while lol, thanks!"

Good: "Explain Python decorators. Include: what they are, syntax, 2 practical examples."

The second message gets a shorter, better-structured answer and costs roughly half the tokens.

---

## Compression Hints for Claude Sonnet

When compressing text for Claude Sonnet, the local model should:

- Use `full` mode by default (Claude handles terse input well)
- Include explicit output format requests: "List:", "Table:", "Steps:", "Code only:"
- Add word limits if you want short answers: "Max 3 sentences.", "One paragraph."
- Claude responds well to role framing even in compressed form: "As senior dev:" or "Plain language:"
- Remove all softening language: "if possible", "when you get a chance", "no rush"

---

## Example Compressions

**Original** (38 words): "I'm trying to understand how to use async/await in Python. Could you explain it with a simple example? I'm a beginner so please keep it simple and avoid jargon."

**Compressed for Claude Sonnet** (15 words): "Python async/await: explain + simple example. Beginner level. No jargon. Max 150 words."

---

## My Background (edit this section)

*Replace this with your own background so the local model can tailor compressions to your context.*

Example: "Software developer, 5 years Python experience, working on web APIs."
Example: "Complete beginner, no coding background, learning AI for marketing."
Example: "Data scientist, familiar with ML concepts, using Claude for code review."
