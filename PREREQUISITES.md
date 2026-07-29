# Prerequisites

Complete this **before** Step 1. Budget 15–30 minutes on a fresh machine.

---

## Checklist

- [ ] VS Code installed  
- [ ] Cline extension installed and signed in / model working  
- [ ] You can open the Cline chat panel and get a short reply  
- [ ] Node.js 18+ (`node -v`, `npx -v`)  
- [ ] Python 3.10+ (`python3 --version` or `python --version`)  
- [ ] `uv` installed ([https://docs.astral.sh/uv/](https://docs.astral.sh/uv/))  
- [ ] Terminal works inside VS Code  
- [ ] Outbound HTTPS works (browser can open [https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true](https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true))  

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

## 3. Node.js (for many community MCP servers)

We use Node/`npx` ecosystem compatibility even though our custom server is Python.

- Download: [https://nodejs.org/](https://nodejs.org/) (LTS)  
- Verify:

```bash
node -v    # v18 or newer
npx -v
```

---

## 4. Python 3.10+

```bash
python3 --version
# Windows may use:
python --version
```

---

## 5. uv (recommended)

`uv` runs Python MCP servers and tools quickly without messy global installs.

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

## 6. Quick network check (weather API)

In a browser or terminal, confirm Open-Meteo responds:

```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" | head -c 300
```

You should see JSON containing `current_weather`.

---

## 7. Know how to open Cline MCP settings

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

## Done?

Continue → [01-add-existing-server/README.md](./01-add-existing-server/README.md)
