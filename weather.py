import requests
import sys
import json


def main(): #Controls all the 3 functions and how they work.
    ...






def lookup():#Looksup the place using Geocode api
    splittest = tests.split(',')
    splittest_1 = splittest[0].strip()
    splittest_2 = splittest[1].strip()
    place = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={'name': tests}) #We request api thru this
    data = place.json()
    for result in data['results']:
        if splittest_1 == result['name'] and splittest_2 == result['country']:
            lat = result['latitude'] #storing lat
            long = result['longitude'] #storing long
            return lat, long





def weather():#Forecast api taking the weather latitude longitude and place
    ...




def formatting():#formats everything after getting the info
    ...



lookup()


