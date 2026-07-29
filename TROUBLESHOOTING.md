# Troubleshooting

## Cline model does not reply

- Confirm provider/API key in Cline settings  
- Try a tiny prompt: `Reply with the single word PONG`  
- Without a working model, tool calling cannot be demonstrated  

## MCP server shows red / disconnected

1. Open Cline → MCP Servers → check error text  
2. Run the same command in a terminal yourself  

**Time server** (local file in this repo):

```bash
# From repo root — should print a datetime dict
uv run --with fastmcp python -c "
import importlib.util
p='01-add-existing-server/time_server.py'
s=importlib.util.spec_from_file_location('t', p)
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
print(m._now_in_tz('Asia/Kolkata'))
"
```

**Weather server:**

```bash
cd 03-build-weather-server/solution
uv run --with fastmcp python -c "import weather_server; print(weather_server.fetch_weather('Chennai'))"
```

Running `uv run --with fastmcp …/time_server.py` (or weather) alone starts **stdio MCP** and looks idle — that is normal. Ctrl+C to stop.

3. Fix JSON commas/brackets in MCP settings  
4. Use **absolute paths** for `time_server.py` and `weather_server.py`  
5. On Windows, prefer forward slashes:

```json
"args": ["run", "--with", "fastmcp", "D:/work/kcg-mcp-workshop/01-add-existing-server/time_server.py"]
```

## `uvx mcp-server-time` ImportError (`McpError` / `MCPError`)

**Do not use** bare `uvx mcp-server-time` for this workshop.  
Upstream packages currently conflict (`McpError` was renamed to `MCPError` in newer `mcp`).

**Fix:** use the in-repo server:

- File: `01-add-existing-server/time_server.py`  
- Cline config: see `01-add-existing-server/cline-mcp.time.example.json`  

If you previously added `uvx` + `mcp-server-time`, replace that entry entirely.

Optional temporary workaround (not recommended for class):

```bash
uvx --with 'mcp>=1.9,<1.10' mcp-server-time --help
```

## Tools list is empty

- Server process crashed on startup (see errors above)  
- Wrong `command` (use full path to `uv` if needed: `which uv` / `where uv`)  
- Restart MCP server from Cline UI, or reload VS Code window  
- Path in `args` is wrong or relative (Cline’s cwd may not be the repo)

## Model replies but never calls the tool

Use stronger prompts from Step 2 / Step 4:

- Include: **“Use your MCP tools. Do not guess.”**  
- Name the tool if needed: **“Call get_current_time”** or **“Call get_current_weather”**  
- Ensure the server is enabled (not `disabled: true`)  
- Check that tools appear in the MCP Servers UI first  

## `uv` not found

- Install uv: https://docs.astral.sh/uv/  
- Restart the terminal **and** VS Code so PATH updates  
- Or set `"command"` to the full path of `uv`  

## Weather tool errors / timeout

- College firewall may block `api.open-meteo.com` or `geocoding-api.open-meteo.com`  
- Test with `curl` from [PREREQUISITES.md](./PREREQUISITES.md)  
- Try another network (phone hotspot)  
- Instructor can demo from a known-good machine  

## `uv run --with fastmcp` is slow first time

First run downloads packages. Wait once; later runs are faster.  
Pre-warm before class:

```bash
uv run --with fastmcp python -c "import fastmcp; print(getattr(fastmcp, '__version__', 'ok'))"
```

## Wrong MCP JSON file edited

Symptoms: your edits never appear in Cline.

Fix: open settings only via **Cline → MCP Servers → Configure → Configure MCP Servers**.

## Permission / auto-approve confusion

Leaving `"autoApprove": []` is fine for learning.  
When Cline asks to run a tool, read the arguments, then approve.

## Python not found when Cline spawns the server

Prefer `uv run` (bundles the env):

```json
"command": "uv",
"args": ["run", "--with", "fastmcp", "/ABS/PATH/time_server.py"]
```

## Still stuck?

1. Compare with `03-build-weather-server/solution/`  
2. Validate JSON with a JSON linter  
3. Ask a facilitator with your OS + screenshot of MCP Servers panel  
