# Examples Publishing & Ingestion (Companion Plan)

This repo is the source of truth for runnable Tactus examples. It contains only the examples and their documentation; all web-facing ingestion lives in the Tactus-web project.

## What lives here
- `.tac` files under `examples/` (organized by category: basics, stdlib, state-sessions, guardrails, evals, durability, models, use-cases, etc.).
- Sibling `.md` docs for each example with frontmatter:
  - `title`, `category`, `tags`
  - `tac` (path to the `.tac` file)
  - `has_specs`, `has_evals`, `requires_api_keys`
  - `summary`
- Optional category `index.md` files.

## What does NOT live here
- No site generation logic. The website ingestion script is in `Tactus-web` (see below).

## Testing (keep examples green)
- Provide a simple runner (e.g., `scripts/test-examples.sh`) that discovers all `.tac` and runs:
  - `tactus test <file> --mock` when specs exist.
  - Optionally `tactus eval <file>` for examples marked `has_evals` (flag to skip in quick CI).
- CI in this repo should fail on broken examples. This keeps the published source of truth healthy.

## Hand-off to the website
- The Tactus-web repo fetches/parses this repo during its build. It does NOT assume a sibling checkout. The ingest script there:
  - Downloads this repo (tarball or shallow clone) if `EXAMPLES_DIR` isn’t provided.
  - Parses the `.md` frontmatter/body to emit `src/data/examples.json` (or MDX) for Gatsby.
- If you change folder names/frontmatter fields here, update the ingest script in Tactus-web accordingly.

## Cross-reference
- The web-side plan lives in `Tactus-web/docs/examples-ingestion-plan.md`.
- When adding examples, keep `.md` + `.tac` in sync and ensure frontmatter is present; otherwise the ingest will skip/mislabel entries.

## Suggested taxonomy (mirror in folder structure)
- `basics/` — hello, params, simple agent, multi-model, streaming.
- `stdlib/` — structured output, JSON parsing, file-io (text/csv/tsv/json/parquet/hdf5/excel), tool schemas/toolsets.
- `state-sessions/` — state, message history, sessions, per-turn tools.
- `guardrails/` — specs, mocking patterns, invariants.
- `evals/` — simple → thresholds → dataset → trace → advanced/comprehensive.
- `durability/` — checkpoints, sub-procedures, script mode.
- `models/` — http/text-classifier/pytorch/multi-model.
- `use-cases/` — text-classification (fuzzy/LLM stdlib), contact-import, meeting-recap-approval, pipelines, compliance-lite.

## Minimal frontmatter template
```
---
title: "Hello World"
category: "basics"
tags: ["hello", "state"]
tac: "examples/basics/01-hello-world.tac"
has_specs: true
has_evals: false
requires_api_keys: false
summary: "Simple hello world with state + output schema."
---
```

Keep this repo lean: examples + docs only. All ingest/build wiring stays in Tactus-web.
