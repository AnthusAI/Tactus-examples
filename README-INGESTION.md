# Examples Publishing & Ingestion

This repo is the source of truth for runnable Tactus examples. It contains only the examples and their documentation; all web-facing ingestion lives in the Tactus-web project.

## What lives here (current structure)

- Numbered chapter directories (e.g. `01-getting-started/`, `02-classification/`).
- Each chapter contains:
  - a `README.md` that describes the examples
  - one or more runnable `.tac` files (single-file examples)
  - optionally, numbered subfolders for multi-file examples

## What does NOT live here
- No site generation logic. The website ingestion script is in `Tactus-web` (see below).

## Testing (keep examples green)
- This repo provides `scripts/test-all.sh` which discovers all `.tac` files and runs:
  - `tactus test <file> --mock` (default) for CI-safe, deterministic checks
  - `scripts/test-all.sh --real` to run against real providers / real models (when configured)
- CI in this repo should fail on broken examples. This keeps the published source of truth healthy.

## Hand-off to the website
- The Tactus-web repo fetches/parses this repo during its build.
- The ingestion code lives in `../Tactus-web/scripts/ingest-examples.js` and it:
  - prefers a sibling checkout (`../Tactus-examples`) when present (for local development)
  - otherwise clones `https://github.com/AnthusAI/Tactus-examples.git` (shallow clone) to a cache directory
  - discovers chapters by numbered folder name (`01-*`, `02-*`, ...)
  - discovers examples as `.tac` files (and certain numbered folders)
  - extracts chapter and example descriptions from each chapter `README.md`
  - heuristically detects `Specification([[...]]])` and `Evaluation([[...]]])` blocks
  - emits `src/data/examples.json` for Gatsby

If you change chapter naming conventions or README structure, update the ingestion script in Tactus-web.

## Adding an example (so the website shows it correctly)

1) Put the new `.tac` file in the relevant chapter folder and give it a numbered prefix:
   - Example: `02-classification/04-model-train-imdb-naive-bayes.tac`
2) Add a section to the chapter `README.md` for the example. Use a heading that includes the example slug:
   - If the file is `04-model-train-imdb-naive-bayes.tac`, the slug is `model-train-imdb-naive-bayes`
   - Add a heading like: `### model-train-imdb-naive-bayes`
3) Ensure the `.tac` contains a `Specification([[...]]])` block so CI stays meaningful.
4) Run `./scripts/test-all.sh` before pushing.

Keep this repo lean: examples + docs only. All ingest/build wiring stays in Tactus-web.
