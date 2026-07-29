# Step 3 — Build your own weather MCP server

**Goal:** Create the simplest useful MCP server: one tool that fetches **live weather** for a city.

**Time:** 25–40 minutes  
**API:** Open-Meteo (free, **no API key**)  
**Language:** Python + MCP FastMCP helper  

---

## Story (why weather?)

| Without a tool | With your MCP tool |
|----------------|--------------------|
| Model guesses or uses stale knowledge | Tool fetches live data |
| Hard to verify | Compare with your phone weather app |
| Not reusable in other clients | Any MCP client can plug into your server |

One sentence:

> **LLMs predict text. Your tool fetches truth.**

---

## What you will ship

| Item | Value |
|------|--------|
| Server name | `weather-tools` |
| Tool name | `get_current_weather` |
| Input | `city: str` (e.g. `"Chennai"`) |
| Output | dict with city, lat, lon, temperature_c, windspeed_kmh, weather, source |

---

## Folders

| Path | Purpose |
|------|---------|
| [`starter/weather_server.py`](./starter/weather_server.py) | **You edit this** |
| [`solution/weather_server.py`](./solution/weather_server.py) | Full working version (spoilers) |
| [`TEST_API.md`](./TEST_API.md) | Open-Meteo cheat sheet |

---

## 3.1 How the tool works

```text
city name
  → Geocoding API  (name → latitude, longitude)
  → Forecast API   (lat/lon → current weather)
  → compact dict returned to Cline
```

Endpoints (details in `TEST_API.md`):

1. `https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1`  
2. `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`  

---

## 3.2 Implement the starter

```bash
cd 03-build-weather-server/starter
```

Open `weather_server.py` and complete every `TODO`.

You only need:

- standard library `urllib` (no pip install required for HTTP)  
- `fastmcp` package at **runtime** via `uv run --with fastmcp` (Step 3.4 / Step 4)

### Tool contract (keep this shape)

Return a dict like:

```python
{
    "city": "Chennai",
    "country": "India",
    "latitude": 13.08,
    "longitude": 80.27,
    "temperature_c": 31.2,
    "windspeed_kmh": 14.5,
    "weather": "Partly cloudy",
    "weather_code": 2,
    "observed_at": "2026-04-01T10:00",
    "source": "open-meteo",
}
```

On failure, return a dict with `"error": "..."` (do not crash the process).

---

## 3.3 Weather code map

Open-Meteo returns a numeric `weathercode`. Map a few common codes to text (already sketched in starter).

---

## 3.4 Smoke-test outside Cline (recommended)

From `starter/`:

```bash
# syntax check
uv run --with fastmcp python -c "import weather_server; print('import-ok')"

# optional: call the pure function if you exposed helpers
uv run --with fastmcp python -c "
import weather_server
print(weather_server.fetch_weather('Chennai'))
"
```

You should see a dict with `temperature_c` or a clear `error`.

> Running `uv run --with fastmcp weather_server.py` alone starts **stdio MCP** and will look “hung”. That is normal. Use Ctrl+C. Cline will spawn it correctly in Step 4.

---

## 3.5 Common mistakes

1. Forgetting to URL-encode the city name  
2. Using the first geocoding result without checking `results` is non-empty  
3. Raising uncaught exceptions (brings down the MCP server process)  
4. Returning long prose instead of structured fields  
5. Editing `solution/` by accident — edit **`starter/`**  

---

## 3.6 If you are blocked (>15 minutes on bugs)

1. Diff against [`solution/weather_server.py`](./solution/weather_server.py)  
2. Or copy solution → starter and read every line  
3. Continue to Step 4 so you still finish the end-to-end loop  

Learning goal is the **MCP loop**, not perfect HTTP parsing under time pressure.

---

## Checkpoint

- [ ] `get_current_weather` defined with a clear docstring  
- [ ] `fetch_weather("Chennai")` returns temperature or a structured error  
- [ ] File path known for Step 4 (you will need the **absolute** path)  

Get absolute path examples:

```bash
# macOS / Linux
realpath weather_server.py

# or
pwd
# then join with /weather_server.py
```

```powershell
# Windows PowerShell
(Resolve-Path .\weather_server.py).Path
```

Continue → [../04-wire-into-cline/README.md](../04-wire-into-cline/README.md)
