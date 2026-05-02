---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---

# Deep Research

[![GitHub](https://img.shields.io/badge/GitHub-repository-181717?logo=github&logoColor=white)](https://github.com/siva-sankari-sivakaminathan/deep_research_openai_agentic_ai)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/UI-Gradio-FF7C00?logo=gradio&logoColor=white)

**Deep Research** is a demo application that turns a research topic into a long, cited markdown report using the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), hosted web search, and a [Gradio](https://gradio.app/) interface.

---

## What it does

1. **Guardrails** — Length limits, basic personal-data pattern checks, and an optional model-based check that the input looks like a research request.
2. **Clarifying questions** — Up to three optional questions to narrow scope before the main run.
3. **Research loop** — A manager agent plans web searches, runs search tools per query term, then merges summaries.
4. **Writing & citations** — A writer produces markdown with numbered references (`[1]`, `[2]`, …) and a **Sources / References** section.
5. **Quality pass** — An evaluator scores the report; an optimizer revises it when refinement is requested.
6. **Exports** — Optional PDF download and optional email delivery via SendGrid.

More detail on components and flow: [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Requirements

- Python 3.11+
- An OpenAI API key with access to the models and tools configured in the agent modules (see `requirements.txt` and agent files).

---

## Installation

```bash
git clone https://github.com/siva-sankari-sivakaminathan/deep_research_openai_agentic_ai.git
cd deep_research_openai_agentic_ai
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set variables (see table below).

---

## Running locally

```bash
python deep_research.py
```

This launches the Gradio UI in the browser. The script enables Gradio’s **share** mode so a temporary `gradio.live` URL can be generated for short-lived public access.

**Alternative entrypoint:** `python app.py` (same UI without `share=True`, suitable for Hugging Face Spaces).

### Environment variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `OPENAI_API_KEY` | Yes | Models, tools, and intent guardrail |
| `SENDGRID_API_KEY` | No | Outbound email from the UI |
| `SENDGRID_FROM_EMAIL` | No | Verified sender domain in SendGrid |
| `DEFAULT_RECIPIENT_EMAIL` | No | Default recipient when none is entered in the UI |

Environment loading: `.env` in the project directory is read first; if absent, the parent directory’s `.env` may be used when this project sits inside a larger checkout.

---

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

Intent-related guardrail tests require `OPENAI_API_KEY` at runtime; otherwise they are skipped.

For CI: configure `OPENAI_API_KEY` as an Actions secret if full test coverage is desired — see [.github/workflows/ci.yml](.github/workflows/ci.yml).

---

## Deploying on Hugging Face Spaces

1. Create a **Gradio** Space.
2. Copy the repository contents into the Space repository root (`app.py`, `deep_research.py`, agent modules, `guardrails.py`, `research_manager.py`, `requirements.txt`, etc.).
3. Set secrets in the Space (minimum: `OPENAI_API_KEY`; optional SendGrid variables for email).

Reference: [Gradio on Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-sdks-gradio).

---

## Security & compliance

- API keys belong in environment variables or platform secrets — not in git history.
- Generated reports reflect retrieved web content; deployers remain responsible for OpenAI, SendGrid, and applicable data-handling policies.

---

## License

[MIT](LICENSE)
