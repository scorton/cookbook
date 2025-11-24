# Scorton VibeNIGHT @42 — Cookbook

This cookbook explains how to use the Scorton VibeNIGHT repo template, covering FastAPI backend duties, Gradio demo wiring, the scortonjs CLI, and VibeTesting scripts. Treat it as a living reference you can update as the stack evolves.

## Quickstart
1. Duplicate the example environment file and install dependencies:
   ```bash
   cp .env.example .env
   make install
   ```
2. Start the services you need:
   ```bash
   make run-backend
   make run-demo
   ```

## Prerequisites
- **Python 3.10+** with a virtual environment tool (e.g., `venv` or `conda`).
- **Node.js 18+** and `npm`/`pnpm` for the scortonjs CLI.
- **Make** for the provided shortcuts.
- Access to any external scoring assets or model weights referenced by `.env`.

## Project layout
The template bundles four pillars:
- `backend/`: FastAPI proxy, scoring utilities, and shared adapters.
- `demo/`: Gradio UI for live interactions and demos.
- `scortonjs/`: Node/TypeScript CLI (scortonjs) for local or CI-driven runs.
- `scripts/vibetesting/`: VibeTesting automation helpers for regression and smoke tests.

Directory names can shift between challenges; rely on `Makefile` targets when in doubt.

## Environment setup
1. Copy `.env.example` to `.env` and fill in secrets (API keys, model paths, or dataset roots).
2. If you need per-service overrides, create files like `backend/.env` or `demo/.env` and load them via your process manager.
3. Re-run `make install` whenever dependencies change to keep Python and Node environments in sync.

## FastAPI backend
- **Run locally:** `make run-backend` (typically wraps `uvicorn backend.main:app --reload`).
- **Add endpoints:** place routers in `backend/routes/` and register them in `backend/main.py`.
- **Scoring helpers:** keep reusable scoring logic in `backend/scoring/`; prefer pure functions for easy testing.
- **Proxy patterns:** isolate external API calls under `backend/clients/` to simplify mocking during VibeTesting.

## Gradio demo
- **Run locally:** `make run-demo` (often wraps `python demo/app.py` or `gradio demo.app:app`).
- **UI hooks:** store callbacks in `demo/handlers.py` and keep UI layout declarations in `demo/interface.py`.
- **Model wiring:** import shared scoring utilities from the backend package instead of duplicating logic.

## scortonjs CLI (Node/TypeScript)
- **Install deps:** from `scortonjs/`, run `npm install` or `pnpm install` (also triggered by `make install`).
- **Build:** `npm run build` to emit compiled JS to `dist/`.
- **Run commands:** `npm start -- <args>` or `node dist/index.js <args>` depending on the script entry.
- **Local linking:** `npm link` lets you invoke the CLI globally as `scortonjs` during development.

## VibeTesting scripts
- **Location:** `scripts/vibetesting/` hosts smoke and regression suites.
- **Usage:** run targeted scripts via `python scripts/vibetesting/<script>.py` or wrap them in `make` targets.
- **Recording baselines:** keep golden outputs under `scripts/vibetesting/baseline/` and document updates in PRs.

## Development workflow
1. Start the backend with reload and the demo UI.
2. Use the Gradio UI to drive sample prompts; capture request/response pairs for automated tests.
3. Encode reproducible scenarios into VibeTesting scripts or the scortonjs CLI.
4. Add unit tests near the logic they cover (e.g., `backend/tests/`, `scortonjs/tests/`).
5. Run linting/formatting before commits (e.g., `ruff`, `mypy`, `eslint`, `prettier`) via `make lint` if provided.

## Troubleshooting
- **Port conflicts:** Adjust `PORT`/`HOST` variables in `.env` or CLI flags for the backend and demo.
- **Dependency drift:** Reinstall with `make install` and clear virtualenvs if you see version mismatch errors.
- **CORS issues:** configure allowed origins in `backend/main.py` middleware when the demo loads remote assets.
- **Slow Gradio reloads:** disable heavy model loads at import time; lazy-load inside callbacks instead.

## Contributing
- Keep changes modular: backend routers, demo UI pieces, CLI commands, and VibeTesting scripts should remain decoupled.
- Document new `make` targets and environment variables directly in this cookbook to keep onboarding smooth.
- Prefer small, focused PRs with demo notes (screenshots or sample commands) when altering UX or scoring behaviors.
