# SKILL.md — Save Token Compression Rules

> **Source**: Adapted from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) — `skills/caveman/SKILL.md`
> **License**: MIT — original work by Julius Brussee. Adapted for Save Token with permission under MIT terms.
> **Purpose**: These rules teach a local AI model to compress verbose English into token-efficient caveman style, then expand it back to clear English for the reader.

---

## What This File Does

When you press **Compress →** in Save Token, the local model reads this file as its instruction manual. It learns exactly *how* to strip your words down to the minimum without losing meaning. When you press **Expand →**, it uses the same rules in reverse to rebuild your readable English.

---

## Compression Levels

### `lite` — Light compression (default, safe for most users)
Remove filler words and unnecessary politeness. Keep full meaning. Good for everyday questions.

**Before**: "Could you please help me understand how I might go about setting up a Python virtual environment on my Windows computer?"
**After**: "How set up Python virtual environment Windows?"

Rules:
- Remove: please, could you, I would like to, I was wondering if, just, basically, essentially, in order to, kind of, sort of, actually, literally, at the end of the day
- Keep: all nouns, verbs, numbers, proper names, file names, error messages
- Shorten: "is not" → "not", "does not" → "no", "I am" → "I", "there is" → "is"
- Preserve question structure so the AI understands what is being asked

---

### `full` — Full caveman compression (recommended for token savings)
Strip to bare minimum. Remove articles, most pronouns, most prepositions. Keep only the load-bearing words.

**Before**: "I am getting a TypeError when I try to import the pandas library. The error says 'No module named pandas' even though I installed it."
**After**: "TypeError import pandas. 'No module named pandas'. Installed already."

Rules:
- Remove: a, an, the, is, are, was, were, be, been, being, have, has, had, do, does, did
- Remove: I, my, me, we, our, you, your, it, its, they, their
- Remove: to, of, in, on, at, by, for, with, from, about, into, through, during, before, after
- Keep: not, no, never, without (negations always kept — removing them changes meaning)
- Keep: all technical terms, error messages, file paths, code snippets, model names
- Keep: question words (what, how, why, when, where, which)
- Format: noun clusters with no articles. "Python file not found error fix" not "fix the error where Python cannot find the file"
- Numbers always kept exactly as written

---

### `ultra` — Maximum compression (advanced users, significant savings)
Every non-essential word removed. Symbols replace words where possible. Abbreviations used freely.

**Before**: "I need to understand the difference between synchronous and asynchronous functions in JavaScript and when I should use one versus the other in a real project."
**After**: "JS sync vs async fn — when use which? Real project context."

Rules:
- Apply all `full` rules plus:
- Use symbols: & (and), → (leads to, results in), = (equals, means), ≠ (not equal, different), + (plus, add), @ (at)
- Use abbreviations: fn (function), var (variable), obj (object), arr (array), str (string), int (integer), bool (boolean), attr (attribute), arg (argument), param (parameter), init (initialise), impl (implement), cfg (config), env (environment), err (error), msg (message), req (request), res (response), db (database), auth (authentication)
- Compress code context: "Python function that takes a list and returns sorted version" → "Python fn: list → sorted"
- Stack related questions: "What is X? How does X work? When should I use X?" → "X: what, how, when use?"

---

### `wenyan-lite` — Classical Chinese style, light
Inspired by Wenyan (文言文) — classical Chinese literary style. Extremely terse, poetic compression. Use for users who enjoy the aesthetic or need maximum brevity.

Applies lite compression rules but additionally:
- Drop subject pronouns entirely (classical style has no mandatory subject)
- Replace "how to" constructions with bare verb phrases
- Use classical connectors: "thus", "therefore", "hence" sparingly
- Short, declarative sentences. No hedging.

**Before**: "Could you please explain how machine learning models are trained and what the backpropagation algorithm does?"
**After**: "Explain ML model training. Backpropagation — what does?"

---

### `wenyan-full` — Classical Chinese style, full
Apply full compression rules in classical style:
- No articles, no pronouns, no prepositions
- Imperative forms only: "Explain", "Show", "List", "Compare", "Fix"
- Three-word minimum sentences where possible
- Colons as connectors: "Python error: no module pandas. Fix?"

**Before**: "I have been trying to get my React application to connect to a FastAPI backend but I keep getting CORS errors and I don't know how to fix them."
**After**: "React app → FastAPI backend: CORS error. Fix?"

---

### `wenyan-ultra` — Classical Chinese style, maximum
Apply ultra compression rules in classical style. Bare essence only.

**Before**: "What are the best practices for writing clean, maintainable code in a large Python codebase with multiple developers?"
**After**: "Large Python codebase, multi-dev: clean code best practices?"

---

## Non-Negotiable Rules (all levels)

1. **Never remove negations** — "not", "no", "never", "without", "don't", "can't", "won't". Removing these reverses meaning.
2. **Never paraphrase technical terms** — error messages, file paths, library names, version numbers, command syntax must be copied exactly.
3. **Never change numbers** — dates, version numbers, quantities, port numbers must be exact.
4. **Preserve the question** — the compressed output must still answer "what does the user want to know or do?"
5. **Code blocks are untouched** — anything inside ``` or ` backticks is copied verbatim, never compressed.
6. **URLs are untouched** — copy URLs exactly as written.
7. **Names are kept** — person names, product names, company names, file names always kept.

---

## Expansion Rules (for MODEL window)

When expanding caveman text back to readable English:

1. Reconstruct full sentences with proper grammar
2. Add articles (a, an, the) where natural
3. Expand abbreviations to full words
4. Add connecting words to make sentences flow
5. Keep all technical terms exactly — never paraphrase code or error messages
6. Match the technical depth of the compressed input — if it was a complex technical question, give a clear technical answer, not a dumbed-down one
7. Do not add opinions, warnings, or extra information not implied by the original
8. Aim for clarity, not verbosity — expanded text should be readable but not padded

---

## Token Savings Reference

Typical savings by level (100-word input):

| Level | Words out | Savings |
|-------|-----------|---------|
| lite | ~65 words | ~35% |
| full | ~30 words | ~70% |
| ultra | ~15 words | ~85% |
| wenyan-lite | ~55 words | ~45% |
| wenyan-full | ~25 words | ~75% |
| wenyan-ultra | ~12 words | ~88% |

Savings vary by content type. Technical questions with long error messages compress less than conversational questions.
