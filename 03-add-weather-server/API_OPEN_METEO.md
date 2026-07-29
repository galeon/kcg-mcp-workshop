# Open-Meteo API cheat sheet

No API key. Be polite with frequency (workshop usage is fine).

## 1) Geocoding — city name → coordinates

```http
GET https://geocoding-api.open-meteo.com/v1/search?name=Chennai&count=1&language=en&format=json
```

Interesting fields in the first result:

- `name`, `country`  
- `latitude`, `longitude`  
- `timezone`  

If `results` is missing or empty → city not found.

## 2) Current weather — coordinates → conditions

```http
GET https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.2785&current_weather=true
```

Interesting fields under `current_weather`:

- `temperature` (°C)  
- `windspeed` (km/h by default in this endpoint)  
- `weathercode` (integer)  
- `time` (ISO-like local timestamp string)  

## 3) Minimal weathercode map (WMO-style, simplified)

| Code | Meaning |
|------|---------|
| 0 | Clear sky |
| 1 | Mainly clear |
| 2 | Partly cloudy |
| 3 | Overcast |
| 45, 48 | Fog |
| 51–57 | Drizzle |
| 61–67 | Rain |
| 71–77 | Snow |
| 80–82 | Rain showers |
| 95–99 | Thunderstorm |

For the workshop, mapping unknowns to `"Unknown (code N)"` is fine.

## 4) Manual test with curl

```bash
curl -s "https://geocoding-api.open-meteo.com/v1/search?name=Chennai&count=1" | head -c 400
curl -s "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true" | head -c 400
```
