# Troubleshooting

## Cline model does not reply

- Confirm provider/API key in Cline settings  
- Try a tiny prompt: `Reply with the single word PONG`  
- Without a working model, tool calling cannot be demonstrated  

## MCP server shows red / disconnected

1. Open Cline → MCP Servers → check error text  
2. Run the same command in a terminal yourself  

Time server:

```bash
uvx mcp-server-time --help
```

Weather server:

```bash
cd 03-build-weather-server/solution
uv run --with fastmcp weather_server.py
```

(A correct stdio server waits silently — that is normal. Ctrl+C to stop.)

3. Fix JSON commas/brackets in MCP settings  
4. Use **absolute paths** for `weather_server.py`  
5. On Windows, use doubled backslashes or forward slashes:

```json
"args": ["run", "--with", "fastmcp", "D:/work/kcg-mcp-workshop/03-build-weather-server/solution/weather_server.py"]
```

## Tools list is empty

- Server process crashed on startup (see errors above)  
- Wrong `command` (use full path to `uv` if needed: `which uv` / `where uv`)  
- Restart MCP server from Cline UI, or reload VS Code window  

## Model replies but never calls the tool

Use stronger prompts from Step 2 / Step 4:

- Include: **“Use your MCP tools. Do not guess.”**  
- Name the tool if needed: **“Call get_current_weather”**  
- Ensure the server is enabled (not `disabled: true`)  
- Check that tools appear in the MCP Servers UI first  

## Time server: `uvx` not found

- Install uv and restart the terminal / VS Code  
- Or set command to the full path of `uvx`  

## Weather tool errors / timeout

- College firewall may block `api.open-meteo.com` or `geocoding-api.open-meteo.com`  
- Test with `curl` from [PREREQUISITES.md](./PREREQUISITES.md)  
- Try another network (phone hotspot)  
- Instructor can demo from a known-good machine  

## `uv run --with fastmcp` is slow first time

First run downloads packages. Wait once; later runs are faster.  
Pre-warm before class:

```bash
uv run --with fastmcp python -c "import fastmcp; print(getattr(fastmcp, "__version__", "ok"))"
```

## Wrong MCP JSON file edited

Symptoms: your edits never appear in Cline.

Fix: open settings only via **Cline → MCP Servers → Configure → Configure MCP Servers**.

## Permission / auto-approve confusion

Leaving `"autoApprove": []` is fine for learning.  
When Cline asks to run a tool, read the arguments, then approve.

## Python not found when Cline spawns the server

Set command to absolute interpreter or rely on `uv run` (preferred):

```json
"command": "uv",
"args": ["run", "--with", "fastmcp", "/ABS/PATH/weather_server.py"]
```

## Still stuck?

1. Compare with `03-build-weather-server/solution/`  
2. Validate JSON with a JSON linter  
3. Ask a facilitator with your OS + screenshot of MCP Servers panel  
