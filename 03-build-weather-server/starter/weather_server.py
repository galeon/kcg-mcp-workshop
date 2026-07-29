#!/usr/bin/env python3
"""
KCG MCP Workshop — STARTER weather MCP server

Complete every TODO, then wire this file into Cline (Step 4).

Run via stdio (Cline does this for you):
  uv run --with fastmcp weather_server.py

Do not worry if this process looks idle when run alone — it speaks MCP on stdin/stdout.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from fastmcp import FastMCP

mcp = FastMCP("weather-tools")

# Simplified WMO weathercode → text
WEATHER_CODES: dict[int, str] = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def _http_get_json(url: str, timeout: float = 15.0) -> dict[str, Any]:
    """GET a URL and parse JSON. Raises urllib.error.URLError / TimeoutError / json errors."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "kcg-mcp-workshop-weather/1.0"},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object from API")
    return data


def weather_description(code: int | None) -> str:
    if code is None:
        return "Unknown"
    return WEATHER_CODES.get(int(code), f"Unknown (code {code})")


def geocode_city(city: str) -> dict[str, Any]:
    """
    Resolve a city name to location fields using Open-Meteo geocoding.

    TODO 1:
      - Build the search URL with urllib.parse.urlencode
      - Call _http_get_json
      - If no results, return {"error": f"City not found: {city}"}
      - Otherwise return a dict with: name, country, latitude, longitude
    """
    city = (city or "").strip()
    if not city:
        return {"error": "city must be a non-empty string"}

    # --- TODO 1: replace this stub ---
    raise NotImplementedError("TODO 1: implement geocode_city")
    # --- end TODO 1 ---


def fetch_current_weather(latitude: float, longitude: float) -> dict[str, Any]:
    """
    Fetch current weather for coordinates.

    TODO 2:
      - Call the Open-Meteo forecast endpoint with current_weather=true
      - Return dict with temperature_c, windspeed_kmh, weather_code, weather, observed_at
      - On missing current_weather, return {"error": "..."}
    """
    # --- TODO 2: replace this stub ---
    raise NotImplementedError("TODO 2: implement fetch_current_weather")
    # --- end TODO 2 ---


def fetch_weather(city: str) -> dict[str, Any]:
    """
    Full pipeline: city → geocode → current weather → single response dict.

    TODO 3:
      - Call geocode_city; if error key present, return it
      - Call fetch_current_weather
      - Merge into the response contract described in the workshop README
      - Never raise — catch Exception and return {"error": str(e)}
    """
    # --- TODO 3: replace this stub ---
    raise NotImplementedError("TODO 3: implement fetch_weather")
    # --- end TODO 3 ---


@mcp.tool()
def get_current_weather(city: str) -> dict[str, Any]:
    """
    Get live current weather for a city name using Open-Meteo (no API key).

    Args:
        city: City name such as "Chennai", "Bengaluru", or "London".

    Returns:
        A dict with temperature_c, windspeed_kmh, weather description, coordinates,
        or an error field if lookup failed.
    """
    # TODO 4: call fetch_weather(city) and return its result
    raise NotImplementedError("TODO 4: wire get_current_weather to fetch_weather")


if __name__ == "__main__":
    # stdio transport — used by Cline / Claude Desktop / other MCP clients
    mcp.run()
