import requests
import sys
import json


def main(): #Controls all the 3 functions and how they work.
    ...






def lookup(name):#Looksup the place using Geocode api
    splittest = name.split(',')
    splittest_1 = splittest[0].strip()
    splittest_2 = splittest[1].strip()
    place = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={'name': name}) #We request api thru this
    data = place.json()
    for result in data['results']:
        if splittest_1 == result['name'] and splittest_2 == result['country']:
            lat = result['latitude'] #storing lat
            long = result['longitude'] #storing long
            return lat, long





def weather(latitude, longitude, unit):#Forecast api taking the weather latitude longitude and place
        #input = input("Input lat and long: ").strip()
        request = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude' : latitude, 'longitude' : longitude, 'current' : 'temperature_2m', 'daily' : 'temperature_2m_max,temperature_2m_min', 'forecast_days' : 4, 'temperature_unit' : unit, 'timezone' : 'auto'})
        data = request.json()
        current_temp = data['current']['temperature_2m']#gets current temperatures
        daily = data['daily']['time'], data['daily']['temperature_2m_max'], data['daily']['temperature_2m_min']#extracts forecast days, max temperatures and minimum temps
        time = daily[0]
        max_temp = daily[1]
        min_temp = daily[2]
        weather_data = {'current_temp': current_temp,'dates': time, 'max_temp' : max_temp, 'min_temp' : min_temp}#organized dict for each value
        return weather_data



def formatting():#formats everything after getting the info
    ...



weather()


