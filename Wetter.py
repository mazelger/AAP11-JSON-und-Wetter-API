import urllib.request
import json

ort = "Innsbruck"
url = f"https://wttr.in/{ort}?format=j1"

# User-Agent setzen, damit JSON korrekt geliefert wird
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req) as response:
    daten = json.loads(response.read().decode())

temperatur = daten["current_condition"][0]["temp_C"]
print(f"In {ort} hat es aktuell {temperatur}°C")
