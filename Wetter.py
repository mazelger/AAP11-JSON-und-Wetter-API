import requests
import json

ort = "Innsbruck"
url = f"https://wttr.in/{ort}?format=j1"

# Anfrage mit requests
response = requests.get(url)
json_string = response.text

# JSON anzeigen
print("JSON String:\n", json_string)

# In Python-Datenstruktur umwandeln
daten = json.loads(json_string)

# Temperatur ausgeben
temperatur = daten["current_condition"][0]["temp_C"]
print(f"Aktuelle Temperatur in {ort}: {temperatur} °C")
