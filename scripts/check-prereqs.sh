#!/usr/bin/env bash
# Quick machine check for KCG MCP Workshop
# Required: Python, uv/uvx, Open-Meteo network
# Optional: Node/npx (not needed for Steps 1–4)
set -euo pipefail

ok() { printf '  [OK] %s\n' "$*"; }
bad() { printf '  [!!] %s\n' "$*"; }
warn() { printf '  [..] %s\n' "$*"; }

echo "KCG MCP Workshop — prerequisite check"
echo "======================================"
echo "Required for Steps 1–4:"
echo

FAIL=0

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
  ok "uvx available (Time server in Step 1)"
else
  bad "uvx not on PATH (install uv and restart the terminal)"
  FAIL=1
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
echo "Optional (not required for this workshop):"
if command -v node >/dev/null 2>&1; then
  ok "node $(node -v) (optional)"
else
  warn "node not found — OK to skip; only needed for npx-based community MCP servers"
fi

if command -v npx >/dev/null 2>&1; then
  ok "npx available (optional)"
else
  warn "npx not found — OK to skip"
fi

echo
if [[ "$FAIL" -eq 0 ]]; then
  echo "Result: ready for Step 1 (still install/configure Cline + model in VS Code)."
  echo "Note: Node/npx are optional and do not block this lab."
  exit 0
else
  echo "Result: fix items marked [!!] before the workshop critical path."
  exit 1
fi
