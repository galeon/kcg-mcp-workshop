# KCG MCP Workshop

**Build and use Model Context Protocol (MCP) tools with VS Code + Cline**

A self-paced, hands-on workshop for college students. You will:

1. Add an **existing** MCP server and **inspect** its tools  
2. Use a **prompt** that calls a tool and returns a real answer  
3. **Create** your own simplest MCP server (live weather)  
4. **Wire** that server into Cline and try it yourself  

No prior MCP experience required. Basic Python + comfort with VS Code helps.

---

## Why this workshop?

Large language models are great at language and weak at **live facts**.

> Ask a chatbot “What’s the weather in Chennai right now?” without tools — it may guess, use stale training data, or refuse.

**MCP** is a standard way to plug **tools** into AI clients (like Cline).  
The model still talks; the **tool** fetches truth.

```text
Your prompt → Cline (MCP client) → MCP server (tools) → real world (time API, weather API)
              ← natural language answer grounded in tool results ←
```

Today you will **consume** a tool, then **produce** one.

---

## Workshop map

| Step | Folder | What you do | Time |
|------|--------|-------------|------|
| 0 | [PREREQUISITES.md](./PREREQUISITES.md) | Install VS Code, Cline, Node, Python, uv | 15–30 min (once) |
| 1 | [01-add-existing-server](./01-add-existing-server/) | Add Time MCP server; inspect tools | 15–20 min |
| 2 | [02-call-a-tool](./02-call-a-tool/) | Prompt Cline so it calls the tool | 10–15 min |
| 3 | [03-build-weather-server](./03-build-weather-server/) | Build `get_current_weather(city)` | 25–40 min |
| 4 | [04-wire-into-cline](./04-wire-into-cline/) | Register your server; try it live | 15–20 min |

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

---

## What you will build

A tiny Python MCP server:

- **Name:** `weather-tools`  
- **Tool:** `get_current_weather(city: str)`  
- **Data:** [Open-Meteo](https://open-meteo.com/) (free, **no API key**)  
- **Returns:** temperature °C, wind, weather description, coordinates  

Starter code (fill in the blanks):  
`03-build-weather-server/starter/weather_server.py`

Working solution (use only if stuck):  
`03-build-weather-server/solution/weather_server.py`

---

## Repository layout

```text
kcg-mcp-workshop/
├── README.md                 ← you are here
├── PREREQUISITES.md
├── TROUBLESHOOTING.md
├── 01-add-existing-server/
├── 02-call-a-tool/
├── 03-build-weather-server/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 04-wire-into-cline/
├── facilitator/              ← for instructors
├── scripts/
└── assets/
```

---

## Learning outcomes

By the end you can:

- Explain MCP in one sentence (client, server, tools)  
- Add a stdio MCP server to **Cline** via JSON config  
- Read a tool’s name, description, and parameters  
- Write a minimal Python MCP server with FastMCP  
- Call your own tool from Cline with a natural-language prompt  

---

## Rules of the road

1. **Use Cline’s MCP settings**, not a random JSON file you found online.  
2. Prefer **absolute paths** in MCP config (especially on Windows).  
3. **Approve tool calls** when Cline asks — know what you are allowing.  
4. Do not commit API keys (this workshop needs none for weather).  
5. If the network blocks Open-Meteo, see [TROUBLESHOOTING.md](./TROUBLESHOOTING.md).

---

## Facilitators

See [facilitator/RUNBOOK.md](./facilitator/RUNBOOK.md) for timing, demo script, and failure recovery.

---

## License

MIT — use freely for teaching and learning.
