# Step 1 — Add an existing MCP server and inspect tools

**Goal:** Connect Cline to a ready-made MCP server and **read** the tools it exposes.

**Time:** 15–20 minutes  
**Server:** Time (`mcp-server-time`) — no API key, works offline after install  

---

## What you will learn

- MCP servers are separate processes Cline starts for you  
- Each server publishes a **tools list** (name, description, parameters)  
- You configure servers with JSON: `command` + `args` (stdio transport)  

---

## 1.1 Why Time (not weather yet)?

We start with **Time** so Step 1 does not depend on campus Wi‑Fi.  
Weather comes when **you** build the server in Step 3.

Mental model:

| Piece | In this step |
|-------|----------------|
| Client | Cline inside VS Code |
| Server | `mcp-server-time` (community/reference style tool) |
| Transport | stdio (Cline runs a local command) |

---

## 1.2 Pre-flight in a terminal

```bash
uvx mcp-server-time --help
```

First run may download the package. That is expected.

If `uvx` is missing, finish [PREREQUISITES.md](../PREREQUISITES.md).

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

Merge the following entry into `mcpServers` (keep any servers you already have).

### macOS / Linux

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### Windows

Often the same, if `uvx` is on PATH:

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

If Cline cannot find `uvx`, use the **full path** from PowerShell:

```powershell
where.exe uvx
```

Example:

```json
"command": "C:\\Users\\YOU\\.local\\bin\\uvx.exe"
```

A copy-paste sample also lives in [`cline-mcp.time.example.json`](./cline-mcp.time.example.json).

Save the file.

---

## 1.5 Verify the server is healthy

1. Return to Cline → **MCP Servers**  
2. Find **time**  
3. It should show as connected / available (not error/red)  
4. Expand it and open the **tools** list  

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

## 1.7 Optional: marketplace path

Some Cline builds offer an MCP marketplace/install UI.  
You may install from there **if** you still end up with a working `time` server and can inspect tools the same way.

If marketplace install fails, use the manual JSON above — it is the reliable path.

---

## Checkpoint

Before Step 2 you must have:

- [ ] `time` server visible in Cline MCP UI  
- [ ] At least one tool listed with name + description + params  
- [ ] Notes from the mini exercise  

Continue → [../02-call-a-tool/README.md](../02-call-a-tool/README.md)
