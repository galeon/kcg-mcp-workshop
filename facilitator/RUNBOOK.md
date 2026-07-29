# Facilitator runbook — KCG MCP Workshop

**Audience:** college students (India-friendly examples; weather is universal)  
**Stack:** VS Code + Cline + Python FastMCP + Open-Meteo  
**Length:** 90–120 minutes (plus prereq time)  
**Pedagogy:** consume working servers first → then read code (no blank starter under time pressure)

---

## Learning goals

Students can:

1. Add an existing MCP server and inspect tools  
2. Trigger a tool call from a natural-language prompt  
3. Add a second complete server (weather) and use it  
4. Explain the Python/FastMCP structure (`FastMCP`, `@mcp.tool`, `mcp.run`, stdio)

---

## Before class (T−1 day)

- [ ] Clone/copy `kcg-mcp-workshop` onto lab image or share Git URL  
- [ ] Pre-install: VS Code, Cline, Python 3.10+, `uv` (Node optional)  
- [ ] Pre-warm caches:

```bash
uv run --with fastmcp python -c "import fastmcp; print('fastmcp-ok')"
uv run --with fastmcp python -c "
import importlib.util
for p in [
  '01-add-existing-server/time_server.py',
  '03-add-weather-server/weather_server.py',
]:
  s=importlib.util.spec_from_file_location('m', p)
  m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
  print(p, 'ok')
"
curl -s "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" | head -c 200
```

- [ ] Confirm Cline model path (shared key / campus proxy / BYO)  
- [ ] Walk the happy path once on lab Wi‑Fi  
- [ ] Backup: hotspot + 60s screen recording  
- [ ] Absolute-path tips for Windows on a slide  

---

## Minute-by-minute (100 min)

| Min | Block | Facilitator | Students |
|-----|-------|-------------|----------|
| 0–8 | Hook | Weather guess vs tool | Open repo in VS Code |
| 8–15 | Prereq triage | Fix Cline/model | `./scripts/check-prereqs.sh` |
| 15–35 | Step 1 | Demo MCP JSON once | Add **time**; inspect tools |
| 35–50 | Step 2 | Project tool call | Time prompts; approve tools |
| 50–55 | Break | — | — |
| 55–75 | Step 3 | Circulate paths | Add **weather**; call Chennai |
| 75–100 | Step 4 | Live code walkthrough | Annotate file; exit ticket |
| 100–110 | Buffer | Unstick | Stretch tool or screenshot |

If **90 min**: shorten Step 4 to sections 4.1–4.4 only; stretch = homework.

---

## Opening monologue (~45s)

> “If I ask an AI the weather in Chennai *right now* and it answers without looking anything up, it is guessing.  
> MCP is a standard plug for tools. Cline is the client.  
> You’ll connect a time tool, watch the model call it, then plug in a complete weather server and use it.  
> After it works, we open the Python file together — FastMCP, tool decorator, stdio — so you see how little code a real MCP server can be.”

---

## Demo script

### A — Time inspect + call
1. Add `time_server.py` with absolute path  
2. Show tools list  
3. Prompt Asia/Kolkata + approve  

### B — Weather second server
1. Terminal `fetch_weather('Chennai')`  
2. Add `weather-tools` JSON  
3. Prompt live weather; compare to phone  

### C — Code walk (projector on weather_server.py)
1. `FastMCP("weather-tools")`  
2. Helpers vs `@mcp.tool`  
3. Docstring → description in UI  
4. `mcp.run()` stdio  
5. Optional: glance at `time_server.py` for two-tool pattern  

---

## Stuck-student policy

| After | Action |
|-------|--------|
| 10 min red time server | Absolute path + `which uv` |
| 10 min red weather | Network curl Open-Meteo; still do Step 4 on code |
| Cline model dead | Fix model before any tool-call grading |

There is **no starter TODO path** — if weather network fails, students still complete inspect-config + code reading.

---

## Exit ticket

1. MCP client we used?  
2. What does `@mcp.tool` do?  
3. Why does running the server alone look “hung”?  
4. Name one field returned by `get_current_weather`.  

---

## Safety

- Leave `autoApprove` empty while teaching  
- No unrestricted filesystem MCP on shared labs  
- Open-Meteo only — no paid keys  
