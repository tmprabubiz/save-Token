# ChatGPT Custom GPT — Template for Save Token Integration

## What Is a Custom GPT?

A Custom GPT is your own personalised version of ChatGPT that you create inside ChatGPT. You give it instructions, and every time you open that Custom GPT, it already knows how to behave. You need a ChatGPT Plus or higher subscription to create Custom GPTs.

Think of it like hiring a personal assistant and giving them a job description — they already know your preferences when they show up.

---

## How to Create a Save Token Custom GPT

Follow these steps. No technical knowledge needed.

**Step 1** — Open ChatGPT
Go to chatgpt.com and sign in. Make sure you have a Plus subscription or higher.

**Step 2** — Go to "My GPTs"
Click your profile picture in the top right corner. Select "My GPTs" from the dropdown menu.

**Step 3** — Create a new GPT
Click "Create a GPT" or "+ Create".

**Step 4** — Skip the chat builder, go to "Configure"
At the top of the creation screen you will see two tabs: "Create" and "Configure". Click **Configure**.

**Step 5** — Fill in the details

- **Name**: `Save Token Reader`
- **Description**: `Reads compressed caveman-style notes and answers in clear English`

**Step 6** — Paste the instructions below
Copy everything between the lines marked START and END and paste it into the **Instructions** field.

---

### START — Paste this into the Custom GPT Instructions field

You are a helpful assistant that understands compressed caveman-style text.

The user will send messages written in a compressed shorthand where:
- Articles (a, an, the) are removed
- Most pronouns are removed
- Filler words and social phrases are stripped out
- Technical terms, error messages, file names, and proper names are kept exactly as written
- Negations (not, no, never, can't, won't) are always kept

Your job is to understand these compressed messages and respond in clear, readable English as if the user had written the full question normally.

When you respond:
- Answer the actual question being asked — interpret the compression charitably
- Keep all technical terms exactly as the user wrote them
- Do not mention that the input was compressed — just answer naturally
- Match the depth: simple compressed questions get clear short answers; complex questions get thorough answers
- Use plain English in your responses unless the user's question is clearly technical

If a compressed message is ambiguous, make the most reasonable interpretation and answer it. Add one sentence: "If you meant something different, clarify [specific ambiguous part]."

Tone: Be direct and helpful. You do not need to use greetings, sign-offs, or filler phrases like "Great question!" or "Certainly!". Just answer.

### END

---

**Step 7** — Set capabilities
Under "Capabilities", enable:
- Web Browsing (optional — turn on if you want the GPT to look things up)
- Code Interpreter (optional — turn on if you ask coding questions)

**Step 8** — Save
Click "Save" in the top right. Choose "Only me" for privacy, or "Anyone with a link" to share.

**Step 9** — Use it with Save Token
When you use Save Token to compress your question:
1. Copy the compressed text from the Save Token checkpoint
2. Open your "Save Token Reader" Custom GPT
3. Paste the compressed text and send it
4. Paste the response back into Save Token's MODEL window to expand it

---

## Notes

- Your Custom GPT is only visible to you unless you choose to share it
- You can edit the instructions at any time: go to "My GPTs" and click the pencil icon
- If you want the GPT to know your background, add it at the bottom of the instructions: "The user is a [your background]. Tailor explanations accordingly."
