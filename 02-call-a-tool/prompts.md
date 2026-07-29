# Step 2 — Prompt cheatsheet

## Time server (should call tools)

```text
What is the current time in Asia/Kolkata? Use get_current_time. Do not guess.
```

```text
Current UTC time via MCP tools only. Reply with ISO-like time.
```

```text
Using tools, compare local time in Asia/Kolkata and America/Los_Angeles in one short sentence.
```

## Control prompts (usually no tools)

```text
Explain stdio vs HTTP MCP transports in two bullet points.
```

```text
What is the difference between an MCP client and an MCP server?
```

## Transition toward weather (tools missing on purpose)

```text
What is the live weather in Coimbatore? Use only tools you already have. If you cannot, say what tool you would need.
```

## After weather server is wired (Step 4)

```text
What is the weather in Chennai right now?
Use the get_current_weather MCP tool. Do not guess temperatures.
```

```text
Call get_current_weather for Bengaluru and summarize temperature_c and weather in one sentence.
```

```text
Use get_current_weather for "Delhi". Return the raw tool fields as a bullet list, then a one-line human summary.
```
