# Architecture (student view)

```text
┌─────────────────────────────────────────────────────────────┐
│  VS Code                                                     │
│   └── Cline  (MCP client)                                    │
│         │ starts process (stdio)                             │
│         ▼                                                    │
│   uv run --with fastmcp time_server.py                       │
│   uv run --with fastmcp weather_server.py                    │
│         │                              │                     │
│         │ tools/list                   │ tools/list          │
│         │ tools/call                   │ tools/call          │
│         ▼                              ▼                     │
│      OS clock / zoneinfo          Open-Meteo HTTPS APIs      │
└─────────────────────────────────────────────────────────────┘
```

## Transports used here

- **stdio** — Cline spawns a local command; talks over stdin/stdout  
- We do **not** use remote HTTP MCP in the critical path (fewer moving parts)

## Packages

| Piece | Package / command |
|-------|-------------------|
| Existing time server (Step 1) | In-repo `01-add-existing-server/time_server.py` via `uv run --with fastmcp` |
| Custom weather server (Step 3–4) | `03-build-weather-server/.../weather_server.py` via `uv run --with fastmcp` |
| Framework | [`fastmcp`](https://gofastmcp.com/) |
| Weather data | Open-Meteo (no API key) |

## Why FastMCP?

It turns a Python function + docstring into an MCP tool (JSON schema included) with very little boilerplate — ideal for a first server.

## Why a local time server (not `uvx mcp-server-time`)?

Public `mcp-server-time` has broken against newer `mcp` releases (`McpError` vs `MCPError`).  
Shipping a tiny pre-built server in the repo keeps the lab reliable while still teaching “configure an existing server.”
