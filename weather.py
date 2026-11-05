import requests
import textwrap

def main(): #Controls all the 3 functions and how they work.
    cc = input("Enter your city and country: ")
    unit = input("Enter your preferred unit: ")
    coordinates = lookup(cc)
    lat, long = coordinates
    weather_data = weather(lat, long, unit)
    report = formatting(weather_data, cc, unit)
    print(report)






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
        request = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude' : latitude, 'longitude' : longitude, 'current' : 'temperature_2m', 'daily' : 'temperature_2m_max,temperature_2m_min', 'forecast_days' : 4, 'temperature_unit' : unit, 'timezone' : 'auto'})
        data = request.json()
        current_temp = data['current']['temperature_2m']#gets current temperatures
        daily = data['daily']['time'], data['daily']['temperature_2m_max'], data['daily']['temperature_2m_min']#extracts forecast days, max temperatures and minimum temps
        time = daily[0]
        max_temp = daily[1]
        min_temp = daily[2]
        weather_data = {'current_temp': current_temp,'dates': time, 'max_temp' : max_temp, 'min_temp' : min_temp}#organized dict for each value
        return weather_data



def formatting(weather_data, city, unit):#formats everything after getting the info
    current_temp = weather_data['current_temp']
    dates = weather_data['dates']
    max_temp = weather_data['max_temp']
    min_temp = weather_data['min_temp']
 #Gets the values of min max temperatures as well as the dates and current temperatures
    forecast_dates = dates[1:4]
    forecast_max_temp = max_temp[1:4]
    forecast_min_temp = min_temp[1:4]
    x = zip(forecast_dates, forecast_max_temp, forecast_min_temp)

    if unit == "celsius":
        display_unit = "°C"
    else:
        display_unit = "°F"

    y = []
    for date, max_temp, min_temp in x:
        daync = (f"{date}: High {max_temp}{display_unit} | Low {min_temp}{display_unit}") #day no current
        y.append(daync)
    oline = "\n".join(y)#one line
    forecast_block = textwrap.indent(oline, "        ")
    report = textwrap.dedent(f"""
        ================================
            {city.upper()} WEATHER
        ================================

        CURRENT CONDITIONS
        Temperature: {current_temp}{display_unit}

        UPCOMING FORECAST\n\n{forecast_block}
        --------------------------------
        Weather data provided by Open-Meteo
        https://open-meteo.com/
    """).strip()
    return report




if __name__ == "__main__":
    main()







