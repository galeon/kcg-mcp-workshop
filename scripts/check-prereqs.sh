#!/usr/bin/env bash
# Quick machine check for KCG MCP Workshop
set -euo pipefail

ok() { printf '  [OK] %s\n' "$*"; }
bad() { printf '  [!!] %s\n' "$*"; }
warn() { printf '  [..] %s\n' "$*"; }

echo "KCG MCP Workshop — prerequisite check"
echo "======================================"

FAIL=0

if command -v node >/dev/null 2>&1; then
  ok "node $(node -v)"
else
  bad "node not found (install Node.js LTS)"
  FAIL=1
fi

if command -v npx >/dev/null 2>&1; then
  ok "npx available"
else
  bad "npx not found"
  FAIL=1
fi

PY=""
if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
fi

if [[ -n "$PY" ]]; then
  ok "$PY $($PY --version 2>&1)"
else
  bad "python3/python not found"
  FAIL=1
fi

if command -v uv >/dev/null 2>&1; then
  ok "uv $(uv --version 2>&1 | tr '\n' ' ')"
else
  bad "uv not found — https://docs.astral.sh/uv/"
  FAIL=1
fi

if command -v uvx >/dev/null 2>&1; then
  ok "uvx available"
else
  warn "uvx not on PATH (usually installed with uv)"
fi

if command -v code >/dev/null 2>&1; then
  ok "VS Code CLI (code) found"
else
  warn "code CLI not on PATH (VS Code may still be installed)"
fi

echo
echo "Network: Open-Meteo"
if command -v curl >/dev/null 2>&1; then
  if curl -fsS --max-time 10 \
    "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" \
    >/dev/null; then
    ok "Open-Meteo forecast reachable"
  else
    bad "Open-Meteo forecast not reachable (weather step may fail on this network)"
    FAIL=1
  fi
else
  warn "curl not found; skip network probe"
fi

echo
if [[ "$FAIL" -eq 0 ]]; then
  echo "Result: ready for Step 1 (still install/configure Cline + model in VS Code)."
  exit 0
else
  echo "Result: fix items marked [!!] before the workshop critical path."
  exit 1
fi
