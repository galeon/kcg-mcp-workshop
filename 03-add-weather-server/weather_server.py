#!/usr/bin/env python3
"""
KCG MCP Workshop — weather MCP server (complete, ready to run)

Live weather via Open-Meteo (no API key).

Students add this as a second MCP server in Cline (Step 3), then study
the code structure in Step 4.

Run under Cline with:
  uv run --with fastmcp /absolute/path/to/weather_server.py
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from fastmcp import FastMCP

mcp = FastMCP("weather-tools")

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
    city = (city or "").strip()
    if not city:
        return {"error": "city must be a non-empty string"}

    qs = urllib.parse.urlencode(
        {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json",
        }
    )
    url = f"https://geocoding-api.open-meteo.com/v1/search?{qs}"
    data = _http_get_json(url)
    results = data.get("results") or []
    if not results:
        return {"error": f"City not found: {city}"}

    top = results[0]
    return {
        "name": top.get("name") or city,
        "country": top.get("country") or "",
        "latitude": float(top["latitude"]),
        "longitude": float(top["longitude"]),
    }


def fetch_current_weather(latitude: float, longitude: float) -> dict[str, Any]:
    qs = urllib.parse.urlencode(
        {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true",
        }
    )
    url = f"https://api.open-meteo.com/v1/forecast?{qs}"
    data = _http_get_json(url)
    current = data.get("current_weather")
    if not isinstance(current, dict):
        return {"error": "Forecast API returned no current_weather"}

    code = current.get("weathercode")
    return {
        "temperature_c": current.get("temperature"),
        "windspeed_kmh": current.get("windspeed"),
        "weather_code": code,
        "weather": weather_description(code if code is None else int(code)),
        "observed_at": current.get("time"),
    }


def fetch_weather(city: str) -> dict[str, Any]:
    try:
        location = geocode_city(city)
        if "error" in location:
            return location

        current = fetch_current_weather(location["latitude"], location["longitude"])
        if "error" in current:
            return current

        return {
            "city": location["name"],
            "country": location["country"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "temperature_c": current["temperature_c"],
            "windspeed_kmh": current["windspeed_kmh"],
            "weather": current["weather"],
            "weather_code": current["weather_code"],
            "observed_at": current["observed_at"],
            "source": "open-meteo",
        }
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP error {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"Network error: {e.reason}"}
    except TimeoutError:
        return {"error": "Request timed out"}
    except Exception as e:  # noqa: BLE001 - keep MCP server alive
        return {"error": str(e)}


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
    return fetch_weather(city)


if __name__ == "__main__":
    mcp.run()
