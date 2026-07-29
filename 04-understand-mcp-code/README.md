# Step 4 — Understand the MCP Python implementation

**Goal:** Read working code and map every important piece to the MCP mental model.

**Time:** 20–30 minutes  
**Files:**

| File | Role |
|------|------|
| [`../03-add-weather-server/weather_server.py`](../03-add-weather-server/weather_server.py) | Full example (tool + HTTP + errors) |
| [`../01-add-existing-server/time_server.py`](../01-add-existing-server/time_server.py) | Simpler example (no network) |

Open **weather_server.py** in VS Code side-by-side with this guide.

---

## 4.1 Big picture (draw this once)

```text
┌──────────────┐  stdio JSON-RPC   ┌─────────────────────┐
│ Cline        │ ◄──────────────► │ weather_server.py   │
│ (MCP client) │  tools/list      │ FastMCP app         │
│              │  tools/call      │  └ get_current_weather
└──────────────┘                  └──────────┬──────────┘
                                             │ HTTPS
                                             ▼
                                      Open-Meteo APIs
```

| Term | In this lab |
|------|-------------|
| **Host / client** | Cline inside VS Code |
| **Server** | Your Python process started by `uv run … weather_server.py` |
| **Transport** | **stdio** (stdin/stdout), not a public HTTP port |
| **Tool** | A function the model may invoke (`get_current_weather`) |
| **Schema** | Auto-built from type hints + docstring |

---

## 4.2 Walk the weather file top → bottom

### A. Imports and server object

```python
from fastmcp import FastMCP

mcp = FastMCP("weather-tools")
```

- **`FastMCP`** = small framework that speaks MCP for you  
- **`"weather-tools"`** = server name (shows up in clients / logs)  
- One process can expose many tools; we expose one for clarity  

Compare with time server: `mcp = FastMCP("time")` — same pattern.

### B. Helpers that are *not* tools

Functions like `_http_get_json`, `geocode_city`, `fetch_current_weather`, `fetch_weather`:

- Normal Python  
- **Not** automatically visible to the model  
- Keep them separate so the **tool** stays a thin, well-named entry point  

**Design lesson:** put messy I/O in helpers; put a clean contract on the tool.

### C. The tool decorator

```python
@mcp.tool()
def get_current_weather(city: str) -> dict[str, Any]:
    """
    Get live current weather for a city name using Open-Meteo (no API key).
    ...
    """
    return fetch_weather(city)
```

What FastMCP does for you:

1. Registers the function as an MCP tool named `get_current_weather`  
2. Builds a **JSON schema** from `city: str`  
3. Uses the **docstring** as the tool description (the model reads this!)  
4. Handles MCP `tools/call` → runs your function → returns the result  

**Try this while reading:** in Cline’s tools list, match:

- tool name ↔ function name  
- description ↔ docstring first lines  
- param `city` ↔ argument `city: str`  

### D. Structured results (and errors)

Happy path returns a **dict** (`temperature_c`, `weather`, …).  
Failures return `{"error": "..."}` instead of crashing.

Why?

- Uncaught exceptions can kill the MCP server process  
- Structured errors still show up as tool results the model can explain  

### E. The entry point

```python
if __name__ == "__main__":
    mcp.run()
```

- Default transport = **stdio**  
- Cline starts this process and talks on pipes  
- If you run it in a terminal alone, it looks “hung” — it is waiting for MCP messages (Ctrl+C)

---

## 4.3 How Cline starts the server (config ↔ process)

```json
"weather-tools": {
  "command": "uv",
  "args": ["run", "--with", "fastmcp", "/ABS/PATH/weather_server.py"]
}
```

| JSON field | Meaning |
|------------|---------|
| key `weather-tools` | Label in Cline UI |
| `command` + `args` | Exact OS process to spawn |
| `uv run --with fastmcp` | Ephemeral env with FastMCP installed |
| absolute path | Stable even if Cline’s cwd is not the repo |

stdio lifecycle:

1. Cline spawns process  
2. Client and server exchange initialize / capabilities  
3. Client calls **tools/list** → your decorated tools appear  
4. On each user task, model may request **tools/call**  
5. Your function runs; result goes back to the model  

---

## 4.4 Time server vs weather server

| Topic | `time_server.py` | `weather_server.py` |
|-------|------------------|---------------------|
| Tools | `get_current_time`, `convert_time` | `get_current_weather` |
| External I/O | none (local clock) | Open-Meteo HTTP |
| Failure modes | bad timezone name | network, unknown city |
| Teaching role | simplest multi-tool server | tool + real API |

Same skeleton both times:

```text
FastMCP(name) → @mcp.tool functions → mcp.run()
```

---

## 4.5 MCP concepts cheat sheet

| Concept | One-liner | In our code? |
|---------|-----------|--------------|
| **Tools** | Actions the model can invoke | `@mcp.tool()` functions |
| **Resources** | Read-only data (files, docs, records) | Not used today (homework) |
| **Prompts** | Server-offered prompt templates | Not used today |
| **stdio transport** | Local subprocess pipes | `mcp.run()` default |
| **HTTP transport** | Remote URL server | Out of scope for this lab |

You only need **tools + stdio** to understand 90% of local MCP demos.

---

## 4.6 Why FastMCP (and what it hides)

Without a helper library you would hand-write JSON-RPC handlers for:

- `initialize`  
- `tools/list`  
- `tools/call`  
- error shapes, content types, etc.  

FastMCP (and similar SDKs) hide that protocol surface so students can focus on:

> **What capability am I giving the agent?**

Production teams still care about auth, timeouts, least privilege, and logging — out of scope here, but the shape is the same.

---

## 4.7 Guided annotation exercise (10 minutes)

In `weather_server.py`, add comments (for yourself) at:

1. `# SERVER: MCP server instance`  
2. `# NOT A TOOL: internal helper` on `geocode_city`  
3. `# TOOL ENTRYPOINT: visible to Cline` on `get_current_weather`  
4. `# STDIO BOOT` on `mcp.run()`  

Then answer in notes:

1. If you renamed `get_current_weather` to `lookup_weather`, what must the user/model do differently?  
2. If you remove the docstring, what gets worse?  
3. Why is absolute path in Cline config important on lab machines?  

---

## 4.8 Stretch (optional homework)

Do **one**:

1. **Add a tool** `get_weather_compare(city_a: str, city_b: str)` that calls `fetch_weather` twice and returns which city is warmer.  
2. **Tighten validation** — reject `city` shorter than 2 characters with a structured error.  
3. **Resource (advanced)** — expose a static markdown resource `workshop://rules` with “always use tools for live weather.”  
4. **Port the pattern** — new file `joke_server.py` is the wrong vibe; better: `campus_echo_server.py` with one tool `echo_upper(text: str)`.

Re-add / restart the server in Cline after code changes.

---

## 4.9 End-of-workshop checklist

- [ ] I can explain client vs server vs tool  
- [ ] I know why stdio servers look idle in a terminal  
- [ ] I can point to `@mcp.tool` and `mcp.run()` in the file  
- [ ] I successfully called **time** and **weather** tools from Cline  
- [ ] I understand live data should come from tools, not model memory  

🎉 You finished the core lab.

---

## Extra reading

- [ARCHITECTURE.md](../ARCHITECTURE.md)  
- [Open-Meteo cheat sheet](../03-add-weather-server/API_OPEN_METEO.md)  
- FastMCP docs: https://gofastmcp.com/  
- MCP intro: https://modelcontextprotocol.io/  
