# Prerequisites

Complete this **before** Step 1. Budget 15–30 minutes on a fresh machine.

---

## Checklist

### Required for this workshop

- [ ] VS Code installed  
- [ ] Cline extension installed and signed in / model working  
- [ ] You can open the Cline chat panel and get a short reply  
- [ ] Python 3.10+ (`python3 --version` or `python --version`)  
- [ ] `uv` installed ([https://docs.astral.sh/uv/](https://docs.astral.sh/uv/))  
- [ ] Terminal works inside VS Code  
- [ ] Outbound HTTPS works (browser can open [https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true](https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true))  

### Optional (not needed for Steps 1–4)

- [ ] Node.js 18+ (`node -v`, `npx -v`) — only if you later try npm/`npx` community MCP servers or some Cline marketplace installs  

**Critical path runtimes:** VS Code + Cline + **Python** + **uv**.  
Time + weather servers both use `uv run --with fastmcp`. **No Node required.**

Optional helper:

```bash
chmod +x scripts/check-prereqs.sh
./scripts/check-prereqs.sh
```

---

## 1. VS Code

Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)

Open this workshop folder:

```bash
code /path/to/kcg-mcp-workshop
```

---

## 2. Cline extension

1. In VS Code: **Extensions** (`Ctrl+Shift+X` / `Cmd+Shift+X`)  
2. Search **Cline**  
3. Install the official Cline extension  
4. Open the Cline panel from the Activity Bar  
5. Configure a model provider (OpenAI, OpenRouter, Anthropic, campus endpoint, etc.)  

**Critical:** You must get a normal chat reply (for example: “Reply with OK”) before continuing.  
MCP labs fail silently when the model backend is broken.

> Workshop organizers: if you provide a shared key or campus proxy, document it here for students.

---

## 3. Python 3.10+

```bash
python3 --version
# Windows may use:
python --version
```

---

## 4. uv (required)

`uv` runs Python MCP servers quickly without messy global installs.  
Both the pre-built Time server and your Weather server start with:

```bash
uv run --with fastmcp /path/to/server.py
```

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# restart terminal, then:
uv --version
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
```

Docs: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

---

## 5. Quick network check (weather API)

In a browser or terminal, confirm Open-Meteo responds:

```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" | head -c 300
```

You should see JSON containing `current_weather`.

---

## 6. Know how to open Cline MCP settings

You will do this often:

1. Open the **Cline** panel in VS Code  
2. Click the **MCP Servers** icon (stacked servers) in the Cline toolbar  
3. Open the **Configure** tab  
4. Click **Configure MCP Servers**  
5. A JSON file opens (Cline MCP settings)  

You will add entries under:

```json
{
  "mcpServers": {
    ...
  }
}
```

### Where the file usually lives

| Platform | Typical path (VS Code extension) |
|----------|-----------------------------------|
| Linux | `~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json` |
| macOS | `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json` |
| Windows | `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json` |
| Cline CLI (if used) | `~/.cline/mcp.json` |

**Always prefer opening the file via Cline → Configure MCP Servers** so you edit the file Cline actually reads.

---

## 7. Node.js (optional)

**Not required** for this workshop’s Steps 1–4.

Install Node only if you want to explore extra community MCP servers that start with `npx`, for example:

```bash
npx -y some-mcp-package
```

- Download: [https://nodejs.org/](https://nodejs.org/) (LTS)  
- Verify:

```bash
node -v    # v18 or newer
npx -v
```

Lab images may still pre-install Node so students can experiment beyond the worksheet; individuals can skip it.

---

## Done?

Continue → [01-add-existing-server/README.md](./01-add-existing-server/README.md)
