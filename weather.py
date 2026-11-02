import requests
import json
place = input("Input your city and country: ")
name = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={'name': place})
data = name.json()


weather = requests.get('https://api.open-meteo.com/v1/forecast')
data = weather.json()
