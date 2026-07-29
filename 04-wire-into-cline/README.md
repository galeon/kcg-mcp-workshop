# Step 4 — Add your weather server to Cline and try it

**Goal:** Register your MCP server in Cline, see `get_current_weather` in the tools list, and call it from a prompt.

**Time:** 15–20 minutes  
**Requires:** Working `weather_server.py` (your starter **or** the solution)

---

## 4.1 Pick which file to run

| If you… | Use this path |
|---------|----------------|
| Finished the starter | `03-build-weather-server/starter/weather_server.py` |
| Are unblocked via solution | `03-build-weather-server/solution/weather_server.py` |

Get the **absolute path** (required):

```bash
# Linux / macOS — example for solution
realpath 03-build-weather-server/solution/weather_server.py
```

```powershell
# Windows PowerShell
(Resolve-Path .\03-build-weather-server\solution\weather_server.py).Path
```

Write it down. You will paste it into JSON.

---

## 4.2 Smoke-test the function once more

```bash
cd 03-build-weather-server/solution   # or starter
uv run --with fastmcp python -c "import weather_server; print(weather_server.fetch_weather('Chennai'))"
```

Expect JSON-like output with `temperature_c` (or a clear `error` if offline).

---

## 4.3 Add server entry in Cline MCP settings

1. Cline → **MCP Servers** → **Configure** → **Configure MCP Servers**  
2. Keep your existing `time` server  
3. Add `weather-tools` beside it  

### Template (macOS / Linux)

Replace `/ABS/PATH/weather_server.py` with your real path.

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"],
      "disabled": false,
      "autoApprove": []
    },
    "weather-tools": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "/ABS/PATH/weather_server.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### Windows notes

- Prefer forward slashes: `D:/work/kcg-mcp-workshop/.../weather_server.py`  
- If `uv` is not on PATH inside VS Code, set `"command"` to the full `uv.exe` path from `where.exe uv`  

Full examples:

- [`cline-mcp.weather.example.json`](./cline-mcp.weather.example.json)  
- [`cline-mcp.full.example.json`](./cline-mcp.full.example.json)  

Save the file.

---

## 4.4 Confirm tools appear

1. Open Cline → **MCP Servers**  
2. `weather-tools` should be connected  
3. Expand tools → you must see **`get_current_weather`**  
4. Read its description and `city` parameter  

If missing, open [TROUBLESHOOTING.md](../TROUBLESHOOTING.md).

---

## 4.5 Call it from a prompt

New Cline chat:

```text
What is the weather in Chennai right now?
Use the get_current_weather MCP tool. Do not guess temperatures.
Summarize temperature_c and weather in one sentence after the tool runs.
```

### Success criteria

- [ ] Cline requests a tool call to `get_current_weather` with `city` ≈ `Chennai`  
- [ ] You approve the call  
- [ ] Tool returns structured fields (or a structured error)  
- [ ] Final answer matches the tool (not a random invented temp)  

### Second try (your city)

```text
Use get_current_weather for "<your city>".
List temperature_c, windspeed_kmh, and weather as bullets, then one emoji summary.
```

### Compare two cities (optional)

```text
Using get_current_weather twice, compare Chennai and Bengaluru temperatures. Which is warmer right now?
```

---

## 4.6 Contrast demo (solidify learning)

Ask **without** insisting on tools first (or in a mode where you refuse tools once):

```text
Roughly how hot is Chennai in April in general?
```

Then:

```text
Live weather in Chennai right now via get_current_weather only.
```

Discuss: general knowledge vs live tool result.

---

## 4.7 Done — what you achieved

You completed the full loop:

1. Consumed someone else’s MCP server (time)  
2. Forced a tool-backed answer  
3. Built your own server (weather)  
4. Plugged it into Cline and used it  

**Career bridge:** companies attach the same kind of tools to agents for GitHub, databases, CRMs, and internal APIs. You just did the smallest real version.

---

## Stretch homework (optional)

1. Add tool `get_weather_compare(city_a: str, city_b: str)`  
2. Add a resource later (advanced): e.g. static `workshop://rules` doc  
3. Package your server so friends can install it with one JSON blob  
4. Swap Open-Meteo for another no-key API and keep the same tool name  

---

## Checkpoint checklist

- [ ] `weather-tools` green/connected in Cline  
- [ ] `get_current_weather` visible in tools list  
- [ ] At least one successful city lookup from chat  
- [ ] You can explain client vs server vs tool in your own words  

🎉 Workshop complete. If something failed, capture a screenshot of MCP Servers + the tool error for your facilitator.
