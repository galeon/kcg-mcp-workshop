# Step 2 — Use a prompt that calls a tool

**Goal:** Make Cline **invoke** an MCP tool and return an answer grounded in the tool result.

**Time:** 10–15 minutes  
**Requires:** Step 1 complete (`time` server healthy)

---

## What you will learn

- Natural language can trigger tool calls  
- You should **see** the tool name and arguments before/when approving  
- Weak prompts → model may answer from memory; strong prompts → tool use  

---

## 2.1 Ground rules

1. Keep the **time** server enabled  
2. Start a **new** Cline task/chat if the old one is messy  
3. When Cline asks permission to run a tool, **read the args**, then approve  
4. Prefer leaving `"autoApprove": []` so you learn the trust boundary  

---

## 2.2 Warm-up prompt (may NOT call a tool)

Paste:

```text
What is MCP in one sentence?
```

Expected: a normal text answer, **no** time tool.  
That is correct — not every question needs tools.

---

## 2.3 Prompt that SHOULD call the time tool

Paste exactly:

```text
What is the current time in Asia/Kolkata?
Use your MCP tools to answer. Do not guess.
After the tool result, reply with the time and timezone only.
```

### What success looks like

1. Cline proposes a tool call (time-related tool from the `time` server)  
2. You approve it  
3. A tool result appears  
4. Final answer includes a concrete time for Asia/Kolkata  

If the model answers with a time **without** any tool call, it may be guessing.  
Say:

```text
You did not use a tool. Call the time MCP tool now for Asia/Kolkata.
```

---

## 2.4 Second prompt (parameter practice)

```text
Give me the current time in America/New_York and Europe/London using tools.
Present a tiny markdown table: timezone | local time.
```

Check that arguments differ per timezone.

---

## 2.5 Observe the loop (draw this once)

```text
You: "time in Asia/Kolkata — use tools"
  → Cline picks tool + fills arguments from the schema
    → MCP server executes
      → tool result (structured or text)
  → Cline writes the final user-facing answer
```

**Key insight:** MCP did not replace the model. It gave the model a **capability**.

---

## 2.6 Failure drill (optional, 3 minutes)

Ask something the time server cannot do:

```text
What is the weather in Chennai right now? Use only currently available MCP tools.
```

Healthy behavior:

- Model admits it has no weather tool, **or**  
- Tries something inappropriate and fails  

Either way, you now feel the gap that **your** weather server will fill in Step 3–4.

---

## Checkpoint

- [ ] You saw at least one real MCP tool invocation for time  
- [ ] You approved a tool call consciously  
- [ ] You can explain: prompt → tool call → result → answer  

Continue → [../03-build-weather-server/README.md](../03-build-weather-server/README.md)

### Prompt cheatsheet

Copy more prompts from [`prompts.md`](./prompts.md).
