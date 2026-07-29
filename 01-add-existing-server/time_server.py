#!/usr/bin/env python3
"""
Pre-built Time MCP server for Step 1–2 of the KCG workshop.

Students do NOT write this file — they only add it to Cline and inspect tools.
(We ship it in-repo so the lab does not depend on a flaky public PyPI tool.)

Run (stdio):
  uv run --with fastmcp /absolute/path/to/time_server.py
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from fastmcp import FastMCP

mcp = FastMCP("time")


def _now_in_tz(tz_name: str) -> dict[str, Any]:
    tz_name = (tz_name or "").strip() or "UTC"
    try:
        if tz_name.upper() == "UTC":
            tz = timezone.utc
        else:
            tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        return {
            "error": f"Unknown timezone: {tz_name}",
            "hint": "Use an IANA name like Asia/Kolkata, America/New_York, Europe/London, or UTC.",
        }

    now = datetime.now(tz)
    dst = now.dst()
    return {
        "timezone": tz_name,
        "datetime": now.isoformat(timespec="seconds"),
        "utc_offset": now.strftime("%z"),
        "day_of_week": now.strftime("%A"),
        "is_dst": bool(dst) and dst.total_seconds() != 0,
    }


@mcp.tool()
def get_current_time(timezone: str = "UTC") -> dict[str, Any]:
    """
    Get the current date and time in a given IANA timezone.

    Args:
        timezone: IANA timezone name, e.g. "Asia/Kolkata", "America/New_York",
                  "Europe/London", or "UTC". Defaults to UTC.
    """
    return _now_in_tz(timezone)


@mcp.tool()
def convert_time(
    source_timezone: str,
    time: str,
    target_timezone: str,
) -> dict[str, Any]:
    """
    Convert a clock time from one timezone to another (today's date in the source zone).

    Args:
        source_timezone: IANA timezone for the input time (e.g. "Asia/Kolkata").
        time: Time of day as HH:MM (24-hour), e.g. "14:30".
        target_timezone: IANA timezone for the output (e.g. "America/New_York").
    """
    try:
        hour_s, minute_s = time.strip().split(":", 1)
        hour, minute = int(hour_s), int(minute_s)
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return {"error": "time must be HH:MM in 24-hour format"}
    except Exception:
        return {"error": "time must be HH:MM in 24-hour format"}

    src = _now_in_tz(source_timezone)
    if "error" in src:
        return src
    tgt_check = _now_in_tz(target_timezone)
    if "error" in tgt_check:
        return tgt_check

    try:
        src_tz = timezone.utc if source_timezone.upper() == "UTC" else ZoneInfo(source_timezone)
        tgt_tz = timezone.utc if target_timezone.upper() == "UTC" else ZoneInfo(target_timezone)
    except ZoneInfoNotFoundError as e:
        return {"error": str(e)}

    # Use "today" in the source timezone
    base = datetime.now(src_tz).replace(hour=hour, minute=minute, second=0, microsecond=0)
    converted = base.astimezone(tgt_tz)
    return {
        "source": {
            "timezone": source_timezone,
            "datetime": base.isoformat(timespec="seconds"),
        },
        "target": {
            "timezone": target_timezone,
            "datetime": converted.isoformat(timespec="seconds"),
            "day_of_week": converted.strftime("%A"),
        },
    }


if __name__ == "__main__":
    mcp.run()
