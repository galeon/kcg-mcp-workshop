# Step 1 — Add an existing MCP server and inspect tools

**Goal:** Connect Cline to a **pre-built** MCP server (you did not write it) and **read** the tools it exposes.

**Time:** 15–20 minutes  
**Server:** Time — shipped in this repo as [`time_server.py`](./time_server.py)  
**Runtime:** `uv` + `fastmcp` (same stack as the weather server later; **no Node**)

> Why not `uvx mcp-server-time`?  
> That public package is currently broken against new `mcp` releases (`McpError` vs `MCPError`).  
> A local pre-built server keeps the lab reliable while still teaching “add someone else’s server.”

---

## What you will learn

- MCP servers are separate processes Cline starts for you  
- Each server publishes a **tools list** (name, description, parameters)  
- You configure servers with JSON: `command` + `args` (stdio transport)  

---

## 1.1 Mental model

| Piece | In this step |
|-------|----------------|
| Client | Cline inside VS Code |
| Server | `time_server.py` (pre-built in this folder) |
| Transport | stdio (Cline runs a local command) |

---

## 1.2 Pre-flight in a terminal

From the **repo root** (`kcg-mcp-workshop`):

```bash
# Resolve absolute path (you will paste this into Cline JSON)
realpath 01-add-existing-server/time_server.py
```

```powershell
# Windows PowerShell
(Resolve-Path .\01-add-existing-server\time_server.py).Path
```

Smoke-test the helpers (optional):

```bash
uv run --with fastmcp python -c "
import importlib.util
p = '01-add-existing-server/time_server.py'
s = importlib.util.spec_from_file_location('t', p)
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
print(m._now_in_tz('Asia/Kolkata'))
"
```

You should see a dict with `datetime` and `timezone`.

> Running the server file alone starts **stdio MCP** and can look “hung”. That is normal. Ctrl+C. Cline will spawn it correctly.

---

## 1.3 Open Cline MCP settings

1. Open the **Cline** panel  
2. Click **MCP Servers** (stacked server icon)  
3. Open **Configure**  
4. Click **Configure MCP Servers**  
5. You should see JSON with a top-level `mcpServers` object  

If the file is empty or new, start from this skeleton:

```json
{
  "mcpServers": {}
}
```

---

## 1.4 Add the Time server

Merge the following into `mcpServers`.  
**Replace** `/ABS/PATH/TO/kcg-mcp-workshop` with your real absolute path from step 1.2.

### macOS / Linux

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
    }
  }
}
```

### Windows

Prefer forward slashes in the path:

```json
{
  "mcpServers": {
    "time": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "D:/path/to/kcg-mcp-workshop/01-add-existing-server/time_server.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

If Cline cannot find `uv`, set `"command"` to the full path from:

```bash
which uv          # macOS / Linux
where.exe uv      # Windows
```

A copy-paste sample also lives in [`cline-mcp.time.example.json`](./cline-mcp.time.example.json).

Save the file.

---

## 1.5 Verify the server is healthy

1. Return to Cline → **MCP Servers**  
2. Find **time**  
3. It should show as connected / available (not error/red)  
4. Expand it and open the **tools** list  

Expected tools (names may match exactly):

- `get_current_time` — current time in a timezone  
- `convert_time` — convert HH:MM between timezones  

If it fails, see [TROUBLESHOOTING.md](../TROUBLESHOOTING.md).

---

## 1.6 Inspect the tools list (do not skip)

For **each** tool you see, write down:

| Field | What to notice |
|-------|----------------|
| **Name** | Exact tool id the model will call |
| **Description** | Natural language — this is how the model knows *when* to use it |
| **Parameters** | JSON schema: required args, types |

### Mini exercise (2 minutes)

Answer in your notes:

1. How many tools does `time` expose?  
2. Which tool would you use for “time in Asia/Kolkata”?  
3. What parameters does that tool need?  

**Teaching point:**  
The model does not magically know the API. It reads this schema.

---

## Checkpoint

Before Step 2 you must have:

- [ ] `time` server visible in Cline MCP UI  
- [ ] At least one tool listed with name + description + params  
- [ ] Notes from the mini exercise  

Continue → [../02-call-a-tool/README.md](../02-call-a-tool/README.md)
