#!/usr/bin/env bash
# Smoke-test the SOLUTION weather helpers (not the MCP stdio loop).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOL="$ROOT/03-build-weather-server/solution"

echo "Testing solution fetch_weather()..."
uv run --with fastmcp python - <<PY
import sys
sys.path.insert(0, r"$SOL")
import weather_server

for city in ("Chennai", "Bengaluru", "NowherevilleXYZ123"):
    result = weather_server.fetch_weather(city)
    print(city, "->", result)
    if city != "NowherevilleXYZ123":
        assert "error" not in result, result
        assert "temperature_c" in result, result
    else:
        assert "error" in result, result
print("smoke-test OK")
PY
