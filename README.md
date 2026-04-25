# 💰 Save Token

**Save money on AI. Learn how AI models work. Keep your questions private.**

---

## 1. What is Save Token and why you need it

Every time you send a message to Claude, GPT-4, or Gemini, you pay per word — or you use up your monthly allowance. Premium AI models are expensive. Heavy users can spend $50–$200 a month or more.

Most of those words are not necessary.

Consider this message: *"Hi! I was just wondering if you could maybe help me understand how Python lists work? I'm a complete beginner and I would really appreciate a simple explanation if that's okay, thank you so much!"*

That is 43 words. The AI model needs only 7: *"Python lists: explain for beginner."*

Same answer. A fraction of the cost.

Save Token is a free desktop tool that does this compression for you. It uses a **local AI model running on your own computer** — one you download once and use forever for free. The local model compresses your question before you send it to the expensive model. When you get a response back, the local model expands it into clear English for you to read.

**You are always in control.** Save Token never sends your text anywhere automatically. You copy and paste — you decide what goes where.

### What you will learn by using it

Over time, you start to see which words carry meaning and which are padding. You naturally start writing more efficient messages. This saves you tokens even when you are not using Save Token.

### The three benefits

1. **Save money** — fewer tokens per message = lower bills
2. **Hit limits less often** — models have daily limits; fewer tokens = more questions per day
3. **Understand AI better** — you see exactly which words matter

---

## 2. What you need before starting

Before you can use Save Token, you need three things on your computer:

1. **Python 3.11 or newer** — a free programming tool (you don't need to know how to code)
2. **Ollama** — a free tool that runs AI models on your own computer
3. **A local AI model** — a small AI model downloaded once, used forever for free
4. **A normal web browser** — Chrome, Firefox, Edge, or Safari

That's it. No cloud accounts needed. No API keys needed to get started.

---

## 3. Which local model to download based on your PC

The model you download depends on your computer's graphics card (GPU). Here is a simple guide:

| Your computer | Chat model | Code model |
|---|---|---|
| **No graphics card** (or old PC) | tinyllama:1.1b | starcoder2:3b |
| **4GB video memory** (e.g. GTX 1660) | phi3:mini | deepseek-coder:1.3b |
| **8GB video memory** (e.g. RTX 2060 Super) ⭐ | gemma3:12b | qwen2.5-coder:7b |
| **16GB+ video memory** (high-end PC) | gemma3:27b | qwen2.5-coder:14b |

> ⭐ **RTX 2060 Super 8GB**: Use the 8GB tier. Both gemma3:12b and qwen2.5-coder:7b fit comfortably.

**Not sure how much video memory you have?** On Windows: press Windows key + R, type `dxdiag`, press Enter, click the Display tab. Look for "Display Memory".

**Download commands** (paste these into a terminal — see INSTALL.md for how to open a terminal):
```
ollama pull gemma3:12b
ollama pull qwen2.5-coder:7b
```

---

## 4. How to start the app

Open a terminal (see INSTALL.md if you don't know how), navigate to the save-Token folder, and run:

```
pip install -r requirements.txt
```

Then choose how you want to open the app:

**In your browser** (classic mode):
```
python app/server.py
```
Then open your browser and go to: **http://localhost:8000**

**As a standalone desktop window** (appears in your taskbar):
```
python launch.py
```
This opens Save Token as a native desktop window — not a browser tab. You can minimise it to the taskbar like any other app.

That's it. Two commands.

---

## 5. How to use Save Token — 6 steps

### Step 1: Open Save Token
Open your browser to http://localhost:8000 (or run `python launch.py` for the desktop window). You will see the 💰 Save Token page with two large text areas and a status line at the bottom showing the local model is connected.

### Step 2: Choose your target AI model (optional but recommended)
In the top right, there are two dropdowns. Click the first one and choose the AI family you will be using (for example: Claude). Then click the second dropdown and choose the specific model (for example: Claude Sonnet). This loads helpful hints into the Personalisation bar.

### Step 3: Add personalisation (optional)
The Personalisation bar lets you describe yourself so the compression is more relevant. For example: *"I am a small business owner asking about accounting software."* This helps the local model understand your context without sending private details to the expensive AI.

### Step 4: Type or paste your question
In the **USER window** (top), type or paste the question you want to send to the AI model. You will see a word count at the bottom right of the window.

### Step 5: Press Compress → and review the checkpoint
Press the **Compress →** button. The local model will process your text (this takes 5–15 seconds). When it is done, a **checkpoint panel** appears between the two windows.

**This is the most important moment.** Read it carefully:
- On the left: your original question and word count
- On the right: the compressed version and new word count
- In the middle: how many words were saved

If you are happy with the compression, press **✓ Copy compressed text**. If something looks wrong or meaning was lost, press **✗ Try again** to re-run.

### Step 6: Send and paste back
- Go to your AI model (Claude, GPT-4, etc.) in your browser
- Paste the compressed text and send it
- Copy the AI's response
- Come back to Save Token and paste it into the **MODEL window** (bottom)
- Press **Expand →** to convert the response back into clear, readable English

---

## 6. What the checkpoint is and why it matters

The checkpoint is the panel that appears between the two windows after compression. It shows you:
- Your original text (left column)
- The compressed version (right column)
- Exactly how many words were saved

**Why can't I skip it?** Because compression is not perfect. Occasionally a word that matters gets removed, or a technical term gets changed. If that happens, you would send an incorrect question to the AI model and get a wrong answer. The checkpoint lets you verify before you copy.

The checkpoint is also the teaching moment. When you see "47 words → 12 words — you saved 74%", you start to understand which parts of your writing carry meaning and which are padding. After a week of using Save Token, you will find yourself writing more efficiently without even thinking about it.

---

## 7. Understanding your logs

Every time you press **Expand →**, Save Token saves the expanded (readable English) response to a log file on your computer. These logs are for your own reference — they are never sent anywhere.

**Where are the logs?**
In the `logs/` folder inside the save-Token directory. For example:
```
save-Token/
└── logs/
    └── 04242026/
        └── 04242026_143201.txt
```

The folder is named by date (month-day-year). The file is named by date and time.

**What is in a log file?**
Each entry looks like this:
```
------------------------------------------------
[04/24/2026 14:32:01]
Model: gemma3:12b | Route: chat | Mode: full
Compressed input: Python lists explain beginner
Expanded output:
Python lists are ordered collections of items. You can store any type of data in a list...
------------------------------------------------
```

**Why only expanded text?**
The log stores the readable English version — what you actually wanted to know. The caveman-style compressed text is just a transit format; it doesn't need to be archived.

---

## 8. Free API key options

You can use Save Token without any API keys at all — just copy and paste to the free versions of Claude, GPT-4, and Gemini in your browser.

If you want to use API keys (for higher limits or to use the models in other tools):

- **Gemini free tier**: Google offers a generous free tier for the Gemini API through Google AI Studio. Visit ai.google.dev to check current limits and get a free key. Search "Gemini API free tier" for tutorial videos — limits change, so check the latest.

- **Groq free tier**: Groq offers fast, free inference for Llama and Mistral models. Visit console.groq.com to sign up. Search "Groq free tier" for current limits and tutorials.

> **Note**: Free tier limits change frequently. Do not rely on specific numbers printed here — always check the official websites.

---

## 9. Common errors in plain English

**"Ollama is not running"**
Ollama needs to be running in the background for Save Token to work. Open a terminal and run `ollama serve`. Leave that terminal window open and try again.

**"Model not found"**
The local model is not downloaded yet. Run `ollama pull gemma3:12b` in a terminal and wait for the download to complete.

**"Port already in use"**
Something else is already using port 8000. Run `python app/server.py --port 8001` and open http://localhost:8001 instead.

**"The local model took too long to respond"**
The first time a model runs after being idle, it takes longer to load. Wait 30 seconds and try again.

**"Cannot connect to the Save Token server"**
The server is not running. Open a terminal, go to the save-Token folder, and run `python app/server.py`.

---

## 10. Credits

Save Token is inspired by and adapted from **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** (MIT License).

The core compression rules in `models/SKILL.md` are adapted from Julius Brussee's original caveman skill file. The concept of compressing natural language to token-efficient shorthand for AI models was pioneered in that project.

**Thank you Julius Brussee for making caveman open source under MIT.**

---

*Save Token is free and open source. Use it, share it, improve it.*
