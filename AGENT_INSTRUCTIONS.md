# Tactus-examples Agent Instructions

This repo is the runnable examples and teaching canon for Tactus.

Core rule: every `.tac` file should either have a `Specification([[ ... ]])`
block or be explicitly marked as a non-testable snippet. Examples should run
in **mock mode** in CI, and optionally in **real mode** when the developer has
providers/models configured.

## Editorial / Quality Rules

Follow `EDITORIAL.md`:
- Code must run.
- Specs must pass.
- Prefer small, teachable examples with clear comments.

## Quality Gates

Primary gate (mock mode):
```bash
./scripts/test-all.sh
```

Optional (real mode; requires API keys / trained models as applicable):
```bash
./scripts/test-all.sh --real
```

Single file:
```bash
python -m tactus.cli.app test path/to/example.tac --mock
python -m tactus.cli.app test path/to/example.tac        # real mode
```

Notes:
- You need Python 3.11+ with `tactus` installed.
- If `../Tactus` is checked out with a venv, `./scripts/test-all.sh` will
  automatically prefer `../Tactus/.venv-py313/bin/python`.

## Canon (Must Match The Main Repo)

- Model training config lives in `Model.training`.
- CLI:
  - Train: `tactus train file.tac --model <name>`
  - Evaluate: `tactus models evaluate file.tac --model <name> [--version ... | --candidate ...]`
- Canonical Model call pattern:
  - `local m = Model("name"); local r = m({ ... }); local out = r.output or r`
- Mocking:
  - `Mocks { ... }` in the same file drives deterministic CI-safe tests.

## Landing The Plane (Session Completion)

Work is not complete until `git push` succeeds.

1. File issues for remaining work
2. Run quality gates (`./scripts/test-all.sh`)
3. Update issue status (close/advance Beads)
4. Push:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # must show up to date
   ```
5. Clean up: clear stashes, prune remote branches
