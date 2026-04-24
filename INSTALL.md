# INSTALL — Save Token Installation Guide

*Step-by-step for Windows, macOS, and Linux. No technical experience needed.*

---

## Before you start

You need:
- An internet connection (for downloading — not needed after installation)
- About 10–15 GB of free disk space (for the AI model)
- 10–20 minutes

---

## Windows Installation

### Step 1 — Install Python 3.11

1. Go to: https://www.python.org/downloads/
2. Click the big yellow button "Download Python 3.11.x" (or newer)
3. Run the downloaded installer
4. **IMPORTANT**: On the first screen, tick the box that says **"Add Python to PATH"**. Do this before clicking Install Now.
5. Click "Install Now"
6. Wait for it to finish. Click Close.

**Verify it worked**: Press Windows key + R, type `cmd`, press Enter. In the black window, type:
```
python --version
```
It should say something like `Python 3.11.9`. If it does, Python is installed correctly.

---

### Step 2 — Install Ollama

1. Go to: https://ollama.com/download
2. Click "Download for Windows"
3. Run the downloaded installer
4. Follow the prompts — just click Next, Next, Install
5. When it finishes, Ollama starts automatically in the background

**Verify it worked**: Open Command Prompt (Windows key + R → `cmd`) and type:
```
ollama --version
```
It should show a version number.

---

### Step 3 — Download your AI model

In Command Prompt, type the command for your hardware (see the table below):

| Your PC | Command |
|---|---|
| No graphics card | `ollama pull tinyllama:1.1b` |
| 4GB video memory | `ollama pull phi3:mini` |
| 8GB video memory (RTX 2060 Super, etc.) | `ollama pull gemma3:12b` |
| 16GB+ video memory | `ollama pull gemma3:27b` |

Also download the code model (for coding questions):

| Your PC | Command |
|---|---|
| No graphics card | `ollama pull starcoder2:3b` |
| 4GB video memory | `ollama pull deepseek-coder:1.3b` |
| 8GB video memory | `ollama pull qwen2.5-coder:7b` |
| 16GB+ video memory | `ollama pull qwen2.5-coder:14b` |

**This download will take a few minutes** depending on your internet speed. The model is 5–8 GB. This is a one-time download.

---

### Step 4 — Get Save Token

**Option A — Download as ZIP (easier)**:
1. Go to the Save Token repository on GitHub
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP to a folder you can find easily (e.g. `C:\Users\YourName\save-Token`)

**Option B — Use Git**:
```
git clone https://github.com/tmprabubiz/save-Token.git
```

---

### Step 5 — Install Python dependencies

Open Command Prompt. Navigate to the save-Token folder:
```
cd C:\Users\YourName\save-Token
```
(Replace the path with wherever you put the folder.)

Then run:
```
pip install -r requirements.txt
```

This installs the few Python libraries Save Token needs. It takes about 30 seconds.

---

### Step 6 — Start Save Token

In the same Command Prompt window, run:
```
python app/server.py
```

You should see:
```
🪨 Save Token starting...
   Open your browser at: http://localhost:8000
   Press Ctrl+C to stop.
```

**Leave this window open.** Don't close it.

---

### Step 7 — Open in browser

Open Chrome, Firefox, or Edge and go to:
```
http://localhost:8000
```

You should see the Save Token interface. The status line at the bottom should say the model is connected and ready.

**Done!** See TUTORIAL.md for how to use it.

---

## macOS Installation

### Step 1 — Install Python 3.11

The easiest way is using Homebrew:

1. Open Terminal (press Cmd + Space, type "Terminal", press Enter)
2. If you don't have Homebrew, install it:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Install Python:
```
brew install python@3.11
```

Or download directly from https://www.python.org/downloads/ and run the macOS installer.

**Verify**: In Terminal, type `python3 --version`. Should say `Python 3.11.x`.

---

### Step 2 — Install Ollama

1. Go to https://ollama.com/download
2. Click "Download for Mac"
3. Open the downloaded file and drag Ollama to your Applications folder
4. Open Ollama from Applications — it appears in your menu bar

---

### Step 3 — Download your AI model

In Terminal:
```
ollama pull gemma3:12b
ollama pull qwen2.5-coder:7b
```

(Adjust based on your Mac's GPU — M1/M2 Macs have unified memory, 8GB+ unified memory uses the 8GB tier)

---

### Steps 4–7 — Same as Windows

Follow Steps 4–7 from the Windows section above, but:
- Use Terminal instead of Command Prompt
- Use `python3` instead of `python` if `python` doesn't work
- Paths use `/` instead of `\`

Start the server:
```
python3 app/server.py
```

---

## Linux Installation

### Step 1 — Install Python 3.11

**Ubuntu / Debian:**
```
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

**Fedora:**
```
sudo dnf install python3.11
```

**Arch:**
```
sudo pacman -S python
```

**Verify**: `python3 --version`

---

### Step 2 — Install Ollama

```
curl -fsSL https://ollama.com/install.sh | sh
```

This installs and starts Ollama as a system service.

---

### Step 3 — Download your AI model

```
ollama pull gemma3:12b
ollama pull qwen2.5-coder:7b
```

---

### Steps 4–7

Same as Windows, using:
- Terminal (already open)
- `python3` instead of `python`
- Forward slashes in paths

---

## LM Studio — Alternative to Ollama

If you prefer LM Studio (a graphical interface for running local models):

1. Download LM Studio from lmstudio.ai
2. Install and open it
3. Click "Search" and find `gemma-3-12b` — download it
4. Click "Local Server" in the left sidebar
5. Select your downloaded model and click "Start Server"

Save Token will automatically detect LM Studio on port 1234. No configuration needed. The status line will say `Backend: lmstudio` when connected.

---

## Keeping Ollama running

On **Windows**: Ollama starts automatically when you log in. If it's not running, search for "Ollama" in the Start menu and open it.

On **macOS**: Ollama runs in the menu bar. Click the icon to check status.

On **Linux**: Ollama runs as a service. Check with `systemctl status ollama`.

If the status line in Save Token says "Ollama is not running", type `ollama serve` in a terminal and leave it open.

---

## Troubleshooting

**pip command not found**
Try `pip3` instead of `pip`. Or: `python -m pip install -r requirements.txt`

**Permission denied errors**
On macOS/Linux, try: `pip install --user -r requirements.txt`

**"No module named fastapi"**
The requirements were not installed. Run `pip install -r requirements.txt` again from the save-Token folder.

**Model download fails halfway**
Run the `ollama pull` command again — it will resume where it left off.

**Port 8000 is already in use**
Try: `python app/server.py` — if it fails, another program is using port 8000. You can edit `app/server.py` and change `port=8000` to `port=8001` near the bottom of the file.
