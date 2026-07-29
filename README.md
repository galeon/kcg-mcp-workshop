# KCG MCP Workshop

**Build and use Model Context Protocol (MCP) tools with VS Code + Cline**

A self-paced, hands-on workshop for college students. You will:

1. Add an **existing** MCP server (time) and **inspect** its tools  
2. Use a **prompt** that calls a tool and returns a real answer  
3. Add a **second** complete server (weather) and try it live  
4. **Read the Python code** and learn how MCP servers are structured  

No prior MCP experience required. Basic Python + comfort with VS Code helps.

---

## Why this workshop?

Large language models are great at language and weak at **live facts**.

> Ask a chatbot “What’s the weather in Chennai right now?” without tools — it may guess, use stale training data, or refuse.

**MCP** is a standard way to plug **tools** into AI clients (like Cline).  
The model still talks; the **tool** fetches truth.

```text
Your prompt → Cline (MCP client) → MCP server (tools) → real world (clock, weather API)
              ← natural language answer grounded in tool results ←
```

Today you **consume** two servers, then **open the code** to see how a server is built — learning from a working implementation instead of blank TODOs under time pressure.

---

## Workshop map

| Step | Folder | What you do | Time |
|------|--------|-------------|------|
| 0 | [PREREQUISITES.md](./PREREQUISITES.md) | VS Code, Cline, Python, uv | 15–30 min (once) |
| 1 | [01-add-existing-server](./01-add-existing-server/) | Add Time MCP; inspect tools | 15–20 min |
| 2 | [02-call-a-tool](./02-call-a-tool/) | Prompt Cline to call time tools | 10–15 min |
| 3 | [03-add-weather-server](./03-add-weather-server/) | Add complete weather MCP; try it | 15–25 min |
| 4 | [04-understand-mcp-code](./04-understand-mcp-code/) | Walk through Python/FastMCP structure | 20–30 min |

**Total:** ~90–120 minutes if prerequisites are done.

---

## Quick start

```bash
# Clone or download this repo, then:
cd kcg-mcp-workshop

# Read prerequisites and complete the checklist
open PREREQUISITES.md   # or open in VS Code

# Optional: verify your machine
./scripts/check-prereqs.sh
```

Then open this folder in **VS Code** and start at Step 1.

Repo: https://github.com/galeon/kcg-mcp-workshop

---

## What you will run

### 1) Time server (pre-built)

- Path: `01-add-existing-server/time_server.py`  
- Tools: `get_current_time`, `convert_time`  

### 2) Weather server (complete sample)

- Path: `03-add-weather-server/weather_server.py`  
- Tool: `get_current_weather(city)`  
- Data: [Open-Meteo](https://open-meteo.com/) (free, **no API key**)  

Both start the same way:

```bash
uv run --with fastmcp /absolute/path/to/server.py
```

---

## Repository layout

```text
kcg-mcp-workshop/
├── README.md
├── PREREQUISITES.md
├── TROUBLESHOOTING.md
├── ARCHITECTURE.md
├── 01-add-existing-server/     ← time server + Step 1
├── 02-call-a-tool/             ← prompts for tool calling
├── 03-add-weather-server/      ← weather server + Step 3
├── 04-understand-mcp-code/     ← code walkthrough (Step 4)
├── facilitator/
├── scripts/
└── assets/
```

---

## Learning outcomes

By the end you can:

- Explain MCP in one sentence (client, server, tools, stdio)  
- Add a stdio MCP server to **Cline** via JSON config  
- Read a tool’s name, description, and parameters  
- Point to `@mcp.tool` and `mcp.run()` in a Python FastMCP server  
- Call time and weather tools from Cline with natural-language prompts  

---

## Rules of the road

1. **Use Cline’s MCP settings**, not a random JSON file you found online.  
2. Prefer **absolute paths** in MCP config (especially on Windows).  
3. **Approve tool calls** when Cline asks — know what you are allowing.  
4. Do not commit API keys (this workshop needs none for weather).  
5. If the network blocks Open-Meteo, see [TROUBLESHOOTING.md](./TROUBLESHOOTING.md).  
6. Do **not** use bare `uvx mcp-server-time` (broken upstream); use the in-repo time server.

---

## Facilitators

See [facilitator/RUNBOOK.md](./facilitator/RUNBOOK.md) for timing, demo script, and failure recovery.

---

## License

MIT — use freely for teaching and learning.
