# Gemini Gems — Template for Save Token Integration

## What Is a Gemini Gem?

A Gem is a custom AI assistant you create inside Google Gemini (you need Gemini Advanced, which requires a Google One AI Premium subscription). You give it a name, a description, and a set of instructions. After that, every conversation you start with that Gem begins with your instructions already loaded — you don't have to paste them every time.

Think of it like creating your own version of Gemini trained to work exactly how you want.

---

## How to Create a Save Token Gem

Follow these steps. No technical knowledge needed.

**Step 1** — Open Gemini
Go to gemini.google.com and sign in. Make sure you have Gemini Advanced.

**Step 2** — Find Gems
On the left side of the screen, look for "Gems" in the sidebar. Click it.

**Step 3** — Create a new Gem
Click the button that says "New Gem" or "+ Create a Gem".

**Step 4** — Name your Gem
Call it: `Save Token Reader`

**Step 5** — Add a description
Type: `Reads compressed caveman-style notes and responds in clear English`

**Step 6** — Paste the instructions below
Copy everything between the lines marked START and END and paste it into the "Instructions" field.

---

### START — Paste this into the Gem instructions field

You are a helpful assistant that understands compressed caveman-style text.

The user will send messages written in a compressed shorthand where:
- Articles (a, an, the) are removed
- Most pronouns are removed
- Filler words are stripped out
- Technical terms and proper names are kept exactly as written
- Negations (not, no, never) are always kept

Your job is to understand these compressed messages and respond in clear, readable English as if the user had written the full question normally.

When you respond:
- Answer the actual question being asked, not a paraphrased version
- Keep technical terms exactly as the user wrote them
- Do not mention that the text was compressed — just answer naturally
- Match the depth of the question: simple questions get simple answers, complex questions get thorough answers
- Always use clear, plain English in your responses

If the compressed text is ambiguous, make a reasonable interpretation and answer that, then add one sentence at the end: "If you meant something different, please clarify [specific point]."

### END

---

**Step 7** — Save
Click "Save" or "Create". Your Gem is now ready.

**Step 8** — Use it with Save Token
When you use Save Token to compress your question:
1. Copy the compressed text from the Save Token checkpoint
2. Open your "Save Token Reader" Gem
3. Paste the compressed text and send it
4. Paste the response back into Save Token's MODEL window to expand it

---

## Notes

- The Gem instructions are loaded fresh at the start of every conversation
- You can update the Gem instructions any time — go back to Gems and edit
- If you want the Gem to also know your background, add it at the bottom of the instructions: "The user is a [your background description]."
