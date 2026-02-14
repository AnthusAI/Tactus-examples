#!/usr/bin/env bash
set -e

MODE="--mock"
if [[ "$1" == "--real" ]]; then
  MODE=""
fi

FAILED=0
PASSED=0

echo "Running Tactus specifications in $([[ -z "$MODE" ]] && echo "REAL" || echo "MOCK") mode..."
echo ""

# Prefer running via the Python module so we don't accidentally pick up an old
# `tactus` executable from a different environment.
#
# CI uses Python 3.11+, but on some dev machines `python3` may be too old.
# We pick a compatible interpreter automatically, with an override via:
#   TACTUS_PYTHON=/path/to/python ./scripts/test-all.sh
PYTHON_BIN="${TACTUS_PYTHON:-}"

if [[ -z "$PYTHON_BIN" ]]; then
  # Dev-friendly: if the main Tactus repo is checked out next to this repo and
  # has a venv, prefer it.
  if [[ -x "../Tactus/.venv-py313/bin/python" ]]; then
    PYTHON_BIN="../Tactus/.venv-py313/bin/python"
  fi
fi

if [[ -z "$PYTHON_BIN" ]]; then
  for candidate in python3.13 python3.12 python3.11 python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then
      if "$candidate" - <<'PY' >/dev/null 2>&1; then
import sys
ok = sys.version_info >= (3, 11)
raise SystemExit(0 if ok else 1)
PY
        PYTHON_BIN="$candidate"
        break
      fi
    fi
  done
fi

if [[ -z "$PYTHON_BIN" ]]; then
  echo "ERROR: Need Python 3.11+ to run Tactus examples." >&2
  echo "Set TACTUS_PYTHON to a compatible interpreter (or use CI)." >&2
  exit 2
fi

TACTUS_CMD=("$PYTHON_BIN" -m tactus.cli.app)

# Find all .tac files excluding hidden directories
while IFS= read -r file; do
  echo "Testing: $file"
  if "${TACTUS_CMD[@]}" test "$file" $MODE; then
    ((PASSED++))
  else
    ((FAILED++))
    echo "❌ FAILED: $file"
  fi
  echo ""
done < <(find . -name "*.tac" -not -path "*/.*" | sort)

echo "================================"
echo "Results: $PASSED passed, $FAILED failed"
echo "================================"

if [[ $FAILED -gt 0 ]]; then
  exit 1
fi
