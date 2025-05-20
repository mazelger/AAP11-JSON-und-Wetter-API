import requests
import json

ort = "Innsbruck"
url = f"https://wttr.in/{ort}?format=j1"

# User-Agent setzen, damit JSON zurückkommt
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
daten = json.loads(response.text)

temperatur = daten["current_condition"][0]["temp_C"]
print(f"In {ort} hat es aktuell {temperatur}°C")
