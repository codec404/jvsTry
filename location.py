import requests

response = requests.get("https://ipinfo.io/json")
geoGet = response.json()
coordinates = geoGet['loc'].split(',')
lat = coordinates[0]
lon = coordinates[1]