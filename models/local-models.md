# Local Models — Hardware Tier Guide

## Copy-paste for chat interface

Paste this as your **first message** or **system prompt** before starting a conversation with your local model:

---

Reply in compressed caveman English. No greet. Drop filler. Short sentences. Key info only. Code: show code first, brief explanation after. No unnecessary intro or recap.

---

## Use with CLI (terminal via Ollama)

```
ollama run gemma3:12b "your question here"
```

For a system prompt with your local model:
```
ollama run gemma3:12b --system "$(cat models/local-models.md)" "your question here"
```

---


## Which model should I download?

This guide tells you which local AI models to use with Save Token based on your computer's hardware. If you are not sure what GPU you have, see the "How to check your GPU" section at the bottom.

---

## Hardware Tiers

| Your PC | Chat Model | Code Model | How to download |
|---|---|---|---|
| No GPU / CPU only | tinyllama:1.1b | starcoder2:3b | `ollama pull tinyllama:1.1b` |
| 4GB VRAM | phi3:mini | deepseek-coder:1.3b | `ollama pull phi3:mini` |
| **8GB VRAM (recommended)** | **gemma3:12b** | **qwen2.5-coder:7b** | `ollama pull gemma3:12b` |
| 16GB+ VRAM | gemma3:27b | qwen2.5-coder:14b | `ollama pull gemma3:27b` |

> **If you have an RTX 2060 Super 8GB, use the 8GB tier. gemma3:12b and qwen2.5-coder:7b both fit comfortably with room to spare.**

---

## What the two models do

**Chat model** (gemma3:12b at 8GB tier):
- Compresses your questions in the USER window
- Expands the AI response in the MODEL window
- Used for all general questions

**Code model** (qwen2.5-coder:7b at 8GB tier):
- Automatically used when Save Token detects code-related content
- Triggered by keywords like `def`, `class`, `function`, `import`, `error:`, etc.
- Better at understanding and compressing technical code questions

---

## Download commands (copy and paste into your terminal)

### No GPU (CPU only)
```
ollama pull tinyllama:1.1b
ollama pull starcoder2:3b
```
*Warning*: These models are slow on CPU. Compression may take 30–60 seconds. The results are usable but not as clean as the GPU-tier models.

### 4GB VRAM (e.g. GTX 1660, RTX 3050, M1/M2 Mac base)
```
ollama pull phi3:mini
ollama pull deepseek-coder:1.3b
```

### 8GB VRAM (e.g. RTX 2060 Super, RTX 3070, RTX 4060)
```
ollama pull gemma3:12b
ollama pull qwen2.5-coder:7b
```

### 16GB+ VRAM (e.g. RTX 3090, RTX 4090, A100, Mac M2 Pro/Max)
```
ollama pull gemma3:27b
ollama pull qwen2.5-coder:14b
```

---

## How to check your GPU (Windows)

1. Press **Windows key + R**
2. Type `dxdiag` and press Enter
3. Click the **Display** tab
4. Look at "Display Memory (VRAM)" — that is your VRAM amount
5. The "Name" field shows your GPU model

---

## How to check your GPU (Linux)

Open a terminal and type:
```
nvidia-smi
```
Look for the "Memory-Usage" column. The total memory shown is your VRAM.

---

## What happens if I use the wrong tier?

- **Too big a model**: Ollama will run it very slowly or give an out-of-memory error. The status bar in Save Token will show this.
- **Too small a model**: Compression works but quality is lower — more meaning may be lost. Still functional.
- **Right model**: Fast (5–15 seconds per compression), clean output, minimal meaning loss.

---

## LM Studio alternative

If you prefer LM Studio over Ollama, the equivalent models are:
- Chat: download `gemma-3-12b` from the Models tab
- Code: download `qwen2.5-coder-7b` from the Models tab

Save Token auto-detects LM Studio on port 1234. No configuration needed.
