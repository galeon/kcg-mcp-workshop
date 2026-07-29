# Facilitator runbook — KCG MCP Workshop

**Audience:** college students (India-friendly examples; weather is universal)  
**Stack:** VS Code + Cline + Python MCP + Open-Meteo  
**Length:** 90–120 minutes (plus prereq time)

---

## Learning goals

Students can:

1. Add an existing MCP server and inspect tools  
2. Trigger a tool call from a natural-language prompt  
3. Build a one-tool weather MCP server  
4. Register it in Cline and use it end-to-end  

---

## Before class (T−1 day)

- [ ] Clone/copy `kcg-mcp-workshop` onto lab image or share Git URL  
- [ ] Pre-install: VS Code, Cline, Node LTS, Python 3.10+, `uv`  
- [ ] Pre-warm caches on one lab account:

```bash
uvx mcp-server-time --help
uv run --with fastmcp python -c "import fastmcp; print('fastmcp-ok')"
curl -s "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" | head -c 200
```

- [ ] Confirm Cline model path (shared key / campus proxy / BYO)  
- [ ] Walk the happy path yourself once on lab Wi‑Fi  
- [ ] Prepare backup: hotspot + 60s screen recording of green path  
- [ ] Print or project absolute-path tips for Windows  

---

## Room setup (T−30 min)

- [ ] Share repo path / zip / Git URL  
- [ ] Slide or whiteboard diagram:

```text
prompt → Cline → MCP server → API/world → tool result → answer
```

- [ ] Write support channel (TA desk / WhatsApp / Slack)  
- [ ] Identify 1–2 roaming TAs for PATH/JSON issues  

---

## Minute-by-minute (100 min version)

| Min | Block | Facilitator does | Students do |
|-----|-------|------------------|-------------|
| 0–8 | Hook + why MCP | Weather guess vs tool story | Listen; open repo in VS Code |
| 8–15 | Prereq triage | Fix broken Cline/model only | `./scripts/check-prereqs.sh` |
| 15–35 | Step 1 | Demo Configure MCP Servers once | Add `time`; inspect tools |
| 35–50 | Step 2 | Project a successful tool call | Run prompts; approve tools |
| 50–55 | Break / catch-up | — | — |
| 55–85 | Step 3 | Circulate; no long lecture | Implement starter TODOs |
| 85–100 | Step 4 | Demo one absolute path config | Wire server; call weather |
| 100–110 | Buffer | Unstick red servers | Stretch or screenshot success |

If only **90 min**, cut Step 2 second prompt and make Step 3 “copy solution after 12 min stuck.”

---

## Opening monologue (~45s)

> “If I ask an AI the weather in Chennai *right now* and it answers without looking anything up, it is guessing or remembering something old.  
> MCP is a standard plug for tools. Cline is the client. Today you’ll connect a ready-made time tool, watch the model call it, then build a weather tool yourself and plug it into Cline.  
> Same pattern companies use to connect agents to GitHub, databases, and internal APIs — we’re just starting with the sky.”

---

## Demo script (projector)

### Demo A — inspect tools
1. Open empty-ish MCP settings  
2. Paste `time` server  
3. Show tools list; zoom on parameters  

### Demo B — tool call
1. Prompt Asia/Kolkata time with “use MCP tools”  
2. Approve tool call slowly so room sees args  

### Demo C — weather (solution path)
1. Show `fetch_weather('Chennai')` in terminal  
2. Add `weather-tools` JSON with **absolute** path  
3. Prompt live weather; approve; compare to phone  

---

## Stuck-student policy

| After | Action |
|-------|--------|
| 10 min on Time server red | Pair with neighbor; TA uses full path to `uvx` |
| 15 min on starter TODOs | Switch to `solution/weather_server.py` |
| Network blocks Open-Meteo | Instructor demo only; student still completes config + inspect tools |
| Cline model dead | Cannot grade tool calling — fix model first |

---

## Checkpoint questions (exit ticket)

1. What is the MCP client in this workshop?  
2. What transport did we use (stdio vs HTTP)?  
3. Why did we build weather instead of only chatting?  
4. Name one field returned by `get_current_weather`.  

---

## Safety & hygiene

- No unrestricted filesystem MCP on shared labs  
- Leave `autoApprove` empty during teaching  
- No student secrets in repo  
- Open-Meteo only — no paid weather keys in critical path  

---

## After class

- Share solution commit / tag  
- Optional homework: `get_weather_compare`  
- Collect 1 photo of MCP tools list per team for attendance/credit if needed  
