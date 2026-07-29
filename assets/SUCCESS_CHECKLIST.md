# Student success checklist

## Prerequisites
- [ ] VS Code + Cline chat works
- [ ] Python + uv installed (Node optional — not required)
- [ ] `./scripts/check-prereqs.sh` mostly green

## Step 1
- [ ] `time` server connected in Cline
- [ ] Tools list inspected (names + params)

## Step 2
- [ ] Prompt caused a time tool call
- [ ] Approved the tool call and got a real timezone answer

## Step 3
- [ ] `weather-tools` connected in Cline
- [ ] `get_current_weather` visible
- [ ] Live city weather via chat (tool call seen)

## Step 4
- [ ] Can point to `FastMCP`, `@mcp.tool`, and `mcp.run()` in the weather file
- [ ] Can explain stdio (“looks hung alone”) in one sentence

## Exit ticket (write answers)
1. MCP client we used: _______________
2. Why weather needs a tool: _______________
3. Absolute path to weather server: _______________
4. What `@mcp.tool` does: _______________
