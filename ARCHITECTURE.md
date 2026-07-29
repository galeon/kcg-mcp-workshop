# Architecture (student view)

```text
┌─────────────────────────────────────────────────────────────┐
│  VS Code                                                     │
│   └── Cline  (MCP client)                                    │
│         │ starts process (stdio)                             │
│         ▼                                                    │
│   uvx mcp-server-time     OR   uv run --with fastmcp server  │
│         │                              │                     │
│         │ tools/list                   │ tools/list          │
│         │ tools/call                   │ tools/call          │
│         ▼                              ▼                     │
│      OS clock                    Open-Meteo HTTPS APIs       │
└─────────────────────────────────────────────────────────────┘
```

## Transports used here

- **stdio** — Cline spawns a local command; talks over stdin/stdout  
- We do **not** use remote HTTP MCP in the critical path (fewer moving parts)

## Packages

| Piece | Package / command |
|-------|-------------------|
| Existing time server | `uvx mcp-server-time` |
| Custom weather server framework | [`fastmcp`](https://gofastmcp.com/) via `uv run --with fastmcp` |
| Weather data | Open-Meteo (no API key) |

## Why FastMCP?

It turns a Python function + docstring into an MCP tool (JSON schema included) with very little boilerplate — ideal for a first server.
