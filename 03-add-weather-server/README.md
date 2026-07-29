# Step 3 — Add the weather MCP server and try it

**Goal:** Add a **second**, complete MCP server (weather), inspect its tools, and call it from Cline.

**Time:** 15–25 minutes  
**Requires:** Steps 1–2 done (`time` server working)  
**Code:** [`weather_server.py`](./weather_server.py) — **already complete** (no starter TODOs)

You are still in “consumer” mode: you did not write this file yet.  
In Step 4 you will open it and learn **how** it implements MCP in Python.

---

## Why weather as server #2?

| Time server | Weather server |
|-------------|----------------|
| Local clock / timezones | Live internet data |
| No network needed | Needs HTTPS (Open-Meteo) |
| Proves tool calling works | Proves tools can reach the real world |

Story:

> The model should not **guess** the temperature. It should **call** `get_current_weather`.

---

## 3.1 Absolute path

From the **repo root**:

```bash
realpath 03-add-weather-server/weather_server.py
```

```powershell
(Resolve-Path .\03-add-weather-server\weather_server.py).Path
```

Write the path down.

---

## 3.2 Optional terminal smoke test

```bash
cd 03-add-weather-server
uv run --with fastmcp python -c "import weather_server; print(weather_server.fetch_weather('Chennai'))"
```

Expect a dict with `temperature_c` (or a clear `error` if the network is blocked).

---

## 3.3 Add `weather-tools` next to `time`

Cline → **MCP Servers** → **Configure** → **Configure MCP Servers**

Keep your existing `time` entry. Add `weather-tools`:

```json
{
  "mcpServers": {
    "time": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "/ABS/PATH/TO/kcg-mcp-workshop/01-add-existing-server/time_server.py"
      ],
      "disabled": false,
      "autoApprove": []
    },
    "weather-tools": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "/ABS/PATH/TO/kcg-mcp-workshop/03-add-weather-server/weather_server.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Copy-paste templates:

- [`cline-mcp.weather.example.json`](./cline-mcp.weather.example.json)  
- [`cline-mcp.full.example.json`](./cline-mcp.full.example.json)  

Save the file.

---

## 3.4 Inspect tools

In Cline → **MCP Servers** → **weather-tools**:

- [ ] Server connected (not red)  
- [ ] Tool **`get_current_weather`** visible  
- [ ] Parameter: `city` (string)  
- [ ] Description mentions live weather / Open-Meteo  

Compare mentally with the time tools: same idea, different domain.

---

## 3.5 Call it from a prompt

New Cline chat:

```text
What is the weather in Chennai right now?
Use the get_current_weather MCP tool. Do not guess temperatures.
Summarize temperature_c and weather in one sentence after the tool runs.
```

### Success criteria

- [ ] Cline proposes `get_current_weather` with `city` ≈ `Chennai`  
- [ ] You approve the tool call  
- [ ] Structured result appears  
- [ ] Final answer matches the tool (not invented)

### More prompts

```text
Use get_current_weather for "Bengaluru". Bullet: temperature_c, windspeed_kmh, weather.
```

```text
Using get_current_weather twice, which is warmer right now: Chennai or Bengaluru?
```

```text
Call get_current_weather for a city near my college. If the tool errors, quote the error field.
```

---

## 3.6 Contrast (optional, 2 minutes)

```text
Roughly how hot is Chennai in a typical April afternoon?
```

Then:

```text
Live weather in Chennai right now via get_current_weather only.
```

Discuss: general knowledge vs live tool result.

---

## Checkpoint

- [ ] Both `time` and `weather-tools` connected  
- [ ] At least one successful weather tool call from chat  
- [ ] You can say in one sentence why weather needed a tool  

Continue → [../04-understand-mcp-code/README.md](../04-understand-mcp-code/README.md)

API reference (optional): [API_OPEN_METEO.md](./API_OPEN_METEO.md)
