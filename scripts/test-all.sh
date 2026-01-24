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

# Find all .tac files excluding hidden directories
while IFS= read -r file; do
  echo "Testing: $file"
  if tactus test "$file" $MODE; then
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
