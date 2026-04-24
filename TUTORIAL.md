# TUTORIAL — Save Token Step by Step

*Written in plain language. Short sentences. Real example.*

---

## Before you start

You have:
- Ollama installed and running (`ollama serve` in a terminal)
- A model downloaded (`ollama pull gemma3:12b`)
- The Save Token server running (`python app/server.py`)
- Your browser open at http://localhost:8000

If any of those are not done yet, see INSTALL.md first.

---

## A complete example — from question to answer

Let's walk through one full session.

---

### What you see when you open Save Token

The screen has:
- A dark top bar with "🪨 Save Token" on the left and dropdowns on the right
- A personalisation box below the top bar
- A large text area labelled "USER — paste or type your question here"
- Below it, a "Compress →" button
- Below that, a large text area labelled "MODEL — paste the AI response here"
- Below that, an "Expand →" button
- At the very bottom, a status line in small text

The status line says something like: `Local model: gemma3:12b | Backend: ollama | 2 model(s) available | Status: ready`

If it says "Connecting to local model..." and then shows an error — see the troubleshooting section below.

---

### Step 1 — Pick your target model (30 seconds)

Top right of the screen. Two dropdowns.

First dropdown: click it. Choose "Claude".
Second dropdown: click it. Choose "Claude Sonnet".

A block of text appears in the personalisation bar. It gives hints about how to write well for Claude Sonnet. Read the first few lines — especially the tone warning.

You don't have to use this feature. You can leave both dropdowns blank and just start compressing.

---

### Step 2 — Write your question (1 minute)

Click in the USER window. Type your question, or paste it from somewhere else.

**What the user typed** (40 words):

> "Hi! I've been struggling to understand how Python virtual environments work and why I need them. I'm a beginner and would really appreciate a clear explanation with maybe a step by step setup guide? Thank you!"

You can see "40 words" in the bottom right of the USER window.

---

### Step 3 — Press Compress → (5–15 seconds)

Press the blue "Compress →" button.

The button shows a spinning circle and says "Compressing...". The status line at the bottom says "Compressing your text...".

Wait. The local model is working.

---

### Step 4 — Read the checkpoint (30 seconds)

A panel appears between the two windows. It has two columns.

**Left column — Your original:**
> Your words: 40

And your original text in a box below.

**Right column — Compressed:**
> Compressed: 9 words

And the compressed text:
> "Python virtual environments: what + why + setup steps. Beginner."

Below the columns:
> Saved **31 words (78%)** — your compressed message is ready to copy.

**Read the compressed text.** Does it still ask what you wanted to ask? Yes — it asks about Python virtual environments, what they are, why they exist, and how to set them up, at beginner level.

If the compression looks wrong — if a key detail was removed or changed — press **✗ Try again**. The model will try once more.

If it looks good, press **✓ Copy compressed text**.

---

### Step 5 — Go to Claude (2 minutes)

Open claude.ai in your browser (or ChatGPT, or Gemini, or whichever model you prefer).

If you set up a Custom GPT or a Gem using the templates in the models/ folder, open that. Otherwise just open a normal chat.

**Paste** the compressed text: "Python virtual environments: what + why + setup steps. Beginner."

Send it.

Claude responds. For example:

> "Python virtual environments are isolated spaces that keep your project's packages separate from your system Python. Use `python -m venv myenv` to create one. Activate with `source myenv/bin/activate` (Mac/Linux) or `myenv\Scripts\activate` (Windows). Then `pip install` inside it stays local to that project."

**Copy** Claude's response.

---

### Step 6 — Expand the response (5–10 seconds)

Come back to Save Token.

Click in the **MODEL window** (bottom large text area). Paste Claude's response.

Press **Expand →**.

The status line says "Expanding compressed response...". A moment later, the MODEL window updates with the expanded version:

> "Python virtual environments are isolated directories that keep your project's Python packages separate from the system-wide Python installation. This prevents version conflicts between different projects. To create one, run `python -m venv myenv` in your project folder. To activate it, run `source myenv/bin/activate` on Mac and Linux, or `myenv\Scripts\activate` on Windows. Once activated, any packages you install with `pip install` will be stored inside that environment and will not affect other projects."

More natural. Better flow. Same information.

**The expansion is also saved to your logs automatically.** You can find it in the `logs/` folder.

---

## What to do when something goes wrong

**The compress button just shows "Compressing..." forever**
The local model is slow on first load. Wait up to 60 seconds. If nothing happens after 60 seconds, check the status line at the bottom — it should say what went wrong.

**The status line says "Ollama is not running"**
Open a terminal and type: `ollama serve`
Leave that window open. Refresh the browser.

**The status line says "No models available"**
Ollama is running but you haven't downloaded a model yet.
In a terminal type: `ollama pull gemma3:12b`
Wait for the download. Then refresh the browser.

**The compression looks completely wrong**
The model occasionally misunderstands. Press **✗ Try again** — the second attempt is usually better. If three attempts all fail badly, try switching to a different compression mode (lite instead of full) using the Mode dropdown in the top right.

**The page just shows a blank white screen**
The Save Token server is not running. Open a terminal, go to the save-Token folder, and run: `python app/server.py`

---

## The three most common user errors

These mistakes happen to everyone. They only waste a few tokens — they do not cause real problems.

### Error 1: Pasting the wrong text in the wrong window

You paste Claude's response into the USER window instead of the MODEL window, then press Compress →. Now you are compressing the AI's answer instead of your question.

**How to spot it**: The checkpoint shows the AI's response being compressed. **What to do**: Click "Try again" or just clear the USER window, paste your question there, and start over.

### Error 2: Forgetting to load the personalisation file into the target model

You created a Claude Custom GPT or Gem but opened a regular Claude chat instead. Your compressed text arrives without context.

**How to spot it**: Claude gives a normal answer without understanding the compressed style. **What to do**: Open your Custom GPT or Gem, or paste the contents of the relevant .md file as a first message. Not a disaster — you just sent a slightly unusual-looking question.

### Error 3: Sending the expanded English to the target model instead of the compressed version

You copied from the right column of the checkpoint (compressed) but then forgot, went away, came back, and copied the wrong thing. You send Claude your full 40-word question instead of the 9-word compressed version.

**How to spot it**: Claude responds normally. **What to do**: Nothing! You got a normal answer. Next time, copy immediately after the checkpoint appears and paste immediately. Don't let time pass between copy and paste.

---

## Summary of one full session

1. Open http://localhost:8000
2. Pick target AI model from dropdowns (optional)
3. Type your question in USER window
4. Press Compress →
5. Read checkpoint — press ✓ Copy if it looks right
6. Go to AI model → paste → send → copy response
7. Paste response in MODEL window
8. Press Expand → read the expanded answer

That's it. You just saved tokens and your session is logged.
