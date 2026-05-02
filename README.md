---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---
# Deep Research (OpenAI Agents + Gradio)

Production-style **deep research** app: input guardrails → clarifying questions → autonomous manager (plan → search → write → evaluate → optimize) → optional email. Uses a **citation layer** (`[1]`, `[2]`, … + Sources section) and the **OpenAI Agents SDK** with **web search**. See [ARCHITECTURE.md](ARCHITECTURE.md) for the flow.

**Features:** Guardrails (intent, PII, length) · Three clarifying questions · Manager with tools · Evaluator–optimizer · Streaming Gradio UI · PDF export · Optional SendGrid email · Hugging Face Space–ready (`app.py`).

## Put this folder on GitHub as its own repo

This directory is **self-contained**: you can publish only `2_openai/deep_research/` as the root of a new repository (recommended if the rest of your `agents` course repo should stay private).

1. On GitHub: **New repository** → create an empty repo (no README if you want a clean first push).
2. On your machine, copy **all files from this folder** into a new directory (or use the folder in place).

   ```powershell
   cd c:\path\to\your\empty\clone
   # copy everything from 2_openai\deep_research\ into here, including .github and .env.example
   ```

3. Initialize and push:

   ```powershell
   git init
   git add -A
   git commit -m "Initial commit: deep research app"
   git branch -M main
   git remote add origin https://github.com/<you>/<your-repo>.git
   git push -u origin main
   ```

4. Add **GitHub Actions** secret **`OPENAI_API_KEY`** (optional) if you want intent guardrail tests to run in CI; without it, those tests are skipped.

Do **not** commit `.env` or real API keys. Use [`.env.example`](.env.example) as a template.

## Run locally

From this folder (whether inside the `agents` monorepo or as a standalone clone):

```bash
pip install -r requirements.txt
# copy .env.example to .env and set OPENAI_API_KEY
python deep_research.py
```

Environment load order: **`.env` in this folder** first, else **`.env` in `2_openai/`** (when nested in the course layout), else process environment.

- **`share=True`** in `deep_research.py` gives a temporary **gradio.live** link.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

## Deploy as a Hugging Face Space

Every **`git push`** to the Space repo updates the live app.

1. [Create a Space](https://huggingface.co/new-space) with SDK **Gradio**.
2. Clone the Space repo and copy **the same files as this folder** into the Space root (including `app.py`, `requirements.txt`, `deep_research.py`, and all `*_agent.py` / `guardrails.py` / `research_manager.py`).
3. Push to Hugging Face.
4. Space **Settings → Secrets**: `OPENAI_API_KEY` (required); optional SendGrid variables for email.

Live URL: `https://huggingface.co/spaces/<username>/<space-name>`.

---

## Quick share (local only)

```bash
python deep_research.py
```

You get localhost plus a **gradio.live** link (public for a limited time).
