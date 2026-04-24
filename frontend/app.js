/**
 * app.js — Save Token frontend logic
 *
 * Handles: compress, checkpoint, expand, model loading,
 * personalisation file loading, word counts, status line.
 */

// ── Model list (Family → Variants) ──────────────────────────────────────────

const MODEL_FAMILIES = [
  {
    family: "Claude",
    variants: [
      { label: "Claude Sonnet",  value: "claude-sonnet",  file: "claude-sonnet.md" },
      { label: "Claude Haiku",   value: "claude-haiku",   file: "claude-haiku.md"  },
      { label: "Claude Opus",    value: "claude-opus",    file: "claude-opus.md"   },
    ],
  },
  {
    family: "GPT-4",
    variants: [
      { label: "GPT-4o",        value: "gpt-4o",       file: "gpt-4o.md"       },
      { label: "GPT-4o mini",   value: "gpt-4o-mini",  file: "gpt-4o-mini.md"  },
      { label: "GPT-4 Turbo",   value: "gpt-4-turbo",  file: "gpt-4-turbo.md"  },
    ],
  },
  {
    family: "Gemini",
    variants: [
      { label: "Gemini 2.0 Flash", value: "gemini-2.0-flash", file: "gemini-2.0-flash.md" },
      { label: "Gemini 2.5 Pro",   value: "gemini-2.5-pro",   file: "gemini-2.5-pro.md"   },
    ],
  },
  {
    family: "Mistral",
    variants: [
      { label: "Mistral Large", value: "mistral-large", file: "mistral-large.md" },
      { label: "Mistral Small", value: "mistral-small", file: "mistral-small.md" },
    ],
  },
  {
    family: "DeepSeek",
    variants: [
      { label: "DeepSeek V3", value: "deepseek-v3", file: "deepseek-v3.md" },
      { label: "DeepSeek R1", value: "deepseek-r1", file: "deepseek-r1.md" },
    ],
  },
  {
    family: "Llama",
    variants: [
      { label: "Llama 3.1 405B", value: "llama3.1-405b", file: "llama3.1-405b.md" },
    ],
  },
  {
    family: "Local",
    variants: [
      { label: "Local models guide", value: "local-models", file: "local-models.md" },
    ],
  },
];

// ── State ────────────────────────────────────────────────────────────────────

let currentBackend = null;    // { type, models }
let lastCompressed = "";      // used after checkpoint copy
let checkpointVisible = false;

// ── DOM References ───────────────────────────────────────────────────────────

const familySelect      = document.getElementById("family-select");
const variantSelect     = document.getElementById("variant-select");
const modeSelect        = document.getElementById("mode-select");
const personaTextarea   = document.getElementById("persona-text");
const loadFileBtn       = document.getElementById("load-file-btn");
const fileInput         = document.getElementById("file-input");

const userTextarea      = document.getElementById("user-text");
const userWordCount     = document.getElementById("user-word-count");
const compressBtn       = document.getElementById("compress-btn");

const checkpointPanel   = document.getElementById("checkpoint-panel");
const origWordEl        = document.getElementById("orig-word-count");
const compWordEl        = document.getElementById("comp-word-count");
const origTextEl        = document.getElementById("orig-text-display");
const compTextEl        = document.getElementById("comp-text-display");
const savingsBadge      = document.getElementById("savings-badge");
const copyCompressedBtn = document.getElementById("copy-compressed-btn");
const tryAgainBtn       = document.getElementById("try-again-btn");

const modelTextarea     = document.getElementById("model-text");
const modelWordCount    = document.getElementById("model-word-count");
const expandBtn         = document.getElementById("expand-btn");

const statusDot         = document.getElementById("status-dot");
const statusText        = document.getElementById("status-text");
const errorBanner       = document.getElementById("error-banner");

// ── Utilities ────────────────────────────────────────────────────────────────

function countWords(text) {
  return text.trim() ? text.trim().split(/\s+/).length : 0;
}

function updateWordCount(textarea, el) {
  el.textContent = `${countWords(textarea.value)} words`;
}

function setStatus(state, message) {
  statusDot.className = "status-dot " + (state || "");
  statusText.textContent = message;
}

function showError(message) {
  errorBanner.textContent = message;
  errorBanner.classList.add("visible");
}

function hideError() {
  errorBanner.classList.remove("visible");
}

// ── Model Family / Variant dropdowns ────────────────────────────────────────

function buildFamilyDropdown() {
  familySelect.innerHTML = '<option value="">— Select target AI —</option>';
  MODEL_FAMILIES.forEach(fam => {
    const opt = document.createElement("option");
    opt.value = fam.family;
    opt.textContent = fam.family;
    familySelect.appendChild(opt);
  });
}

function buildVariantDropdown(familyName) {
  variantSelect.innerHTML = '<option value="">— Variant —</option>';
  if (!familyName) return;
  const fam = MODEL_FAMILIES.find(f => f.family === familyName);
  if (!fam) return;
  fam.variants.forEach(v => {
    const opt = document.createElement("option");
    opt.value = v.value;
    opt.dataset.file = v.file;
    opt.textContent = v.label;
    variantSelect.appendChild(opt);
  });
}

familySelect.addEventListener("change", () => {
  buildVariantDropdown(familySelect.value);
});

variantSelect.addEventListener("change", async () => {
  const selected = variantSelect.options[variantSelect.selectedIndex];
  if (!selected || !selected.dataset.file) return;
  await loadPersonaFromServer(selected.dataset.file);
});

// ── Load personalisation file ────────────────────────────────────────────────

async function loadPersonaFromServer(filename) {
  try {
    const resp = await fetch(`/static/models_content/${filename}`);
    if (!resp.ok) {
      // Fall back: try loading from models directory via a dedicated endpoint
      const resp2 = await fetch(`/model-persona/${filename}`);
      if (!resp2.ok) return;
      const text = await resp2.text();
      personaTextarea.value = text;
      return;
    }
    const text = await resp.text();
    personaTextarea.value = text;
  } catch (e) {
    // Silent — persona loading is optional
  }
}

// File picker fallback
loadFileBtn.addEventListener("click", () => fileInput.click());
fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    personaTextarea.value = e.target.result;
  };
  reader.readAsText(file);
  fileInput.value = "";
});

// ── Word count live updates ──────────────────────────────────────────────────

userTextarea.addEventListener("input", () => updateWordCount(userTextarea, userWordCount));
modelTextarea.addEventListener("input", () => updateWordCount(modelTextarea, modelWordCount));

// ── Health check on load ─────────────────────────────────────────────────────

async function checkHealth() {
  setStatus("loading", "Connecting to local model...");
  try {
    const resp = await fetch("/health");
    const data = await resp.json();
    if (data.status === "ok") {
      currentBackend = { type: data.backend, models: data.models };
      const modelCount = data.models.length;
      const firstModel = data.models[0] || "unknown";
      setStatus("ok", `Local model: ${firstModel} | Backend: ${data.backend} | ${modelCount} model(s) available | Status: ready`);
      hideError();
    } else {
      setStatus("error", data.message || "Local model not available");
      showError(data.message || "Could not connect to local model. Please start Ollama and try again.");
    }
  } catch (e) {
    setStatus("error", "Cannot reach Save Token server — is it running?");
    showError("Cannot connect to the Save Token server. Please start the server: run 'python app/server.py' in your terminal, then refresh this page.");
  }
}

// ── Compress ─────────────────────────────────────────────────────────────────

compressBtn.addEventListener("click", runCompress);

async function runCompress() {
  const text = userTextarea.value.trim();
  if (!text) {
    showError("Please type or paste your question in the USER window first.");
    return;
  }

  hideError();
  hideCheckpoint();

  const mode = modeSelect.value;
  const personalisation = personaTextarea.value.trim();

  // Show loading state
  compressBtn.disabled = true;
  compressBtn.innerHTML = '<span class="spinner"></span>Compressing...';
  setStatus("loading", "Compressing your text...");

  try {
    const resp = await fetch("/compress", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, mode, personalisation }),
    });

    const data = await resp.json();

    if (!resp.ok) {
      const msg = data.detail || "Compression failed. Please try again.";
      showError(msg);
      setStatus("error", msg);
      return;
    }

    // Show checkpoint
    showCheckpoint(text, data);
    setStatus("ok",
      `Local model: ${data.model_used} | Route: ${data.route} | ${data.route_reason} | Status: ready`
    );

  } catch (e) {
    const msg = "Could not compress text. Please check that the server is running.";
    showError(msg);
    setStatus("error", msg);
  } finally {
    compressBtn.disabled = false;
    compressBtn.textContent = "Compress →";
  }
}

// ── Checkpoint ───────────────────────────────────────────────────────────────

function showCheckpoint(originalText, data) {
  origWordEl.textContent = `Your words: ${data.original_words}`;
  compWordEl.textContent = `Compressed: ${data.compressed_words} words`;
  compWordEl.className = "checkpoint-col-count savings";
  origTextEl.textContent = originalText;
  compTextEl.textContent = data.compressed;
  savingsBadge.innerHTML =
    `Saved <strong>${data.words_saved} words (${data.percent_saved}%)</strong> — your compressed message is ready to copy.`;

  lastCompressed = data.compressed;
  copyCompressedBtn.disabled = false;

  checkpointPanel.classList.add("visible");
  checkpointVisible = true;
  checkpointPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function hideCheckpoint() {
  checkpointPanel.classList.remove("visible");
  checkpointVisible = false;
  copyCompressedBtn.disabled = true;
  lastCompressed = "";
}

copyCompressedBtn.addEventListener("click", () => {
  if (!lastCompressed) return;
  navigator.clipboard.writeText(lastCompressed).then(() => {
    copyCompressedBtn.textContent = "✓ Copied!";
    setTimeout(() => {
      copyCompressedBtn.textContent = "✓ Copy compressed text";
    }, 2000);
  }).catch(() => {
    // Fallback for browsers that block clipboard API
    const ta = document.createElement("textarea");
    ta.value = lastCompressed;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    document.body.removeChild(ta);
    copyCompressedBtn.textContent = "✓ Copied!";
    setTimeout(() => {
      copyCompressedBtn.textContent = "✓ Copy compressed text";
    }, 2000);
  });
});

tryAgainBtn.addEventListener("click", () => {
  hideCheckpoint();
  runCompress();
});

// ── Expand ───────────────────────────────────────────────────────────────────

expandBtn.addEventListener("click", async () => {
  const text = modelTextarea.value.trim();
  if (!text) {
    showError("Please paste the AI model's response in the MODEL window first.");
    return;
  }

  hideError();

  expandBtn.disabled = true;
  expandBtn.innerHTML = '<span class="spinner"></span>Expanding...';
  setStatus("loading", "Expanding compressed response...");

  try {
    const resp = await fetch("/expand", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await resp.json();

    if (!resp.ok) {
      const msg = data.detail || "Expansion failed. Please try again.";
      showError(msg);
      setStatus("error", msg);
      return;
    }

    // Replace MODEL window content with expanded text
    modelTextarea.value = data.expanded;
    updateWordCount(modelTextarea, modelWordCount);
    setStatus("ok",
      `Local model: ${data.model_used} | Route: expand | Status: ready — response expanded and logged`
    );

  } catch (e) {
    const msg = "Could not expand text. Please check that the server is running.";
    showError(msg);
    setStatus("error", msg);
  } finally {
    expandBtn.disabled = false;
    expandBtn.textContent = "Expand →";
  }
});

// ── Init ─────────────────────────────────────────────────────────────────────

buildFamilyDropdown();
checkHealth();
updateWordCount(userTextarea, userWordCount);
updateWordCount(modelTextarea, modelWordCount);
