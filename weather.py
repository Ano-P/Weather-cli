import requests
import textwrap
import sys

def main(): #Controls all the 3 functions and how they work.
    cc = input("Enter your city and country: ").strip()
    if cc == "":
        sys.exit("Not a valid input. ")
    elif cc.count(",") != 1:
        sys.exit("Error, Invalid input ")
    cc_ = cc.split(",")

    city = cc_[0].strip()
    country = cc_[1].strip()

    if city == "" or country == "":
        sys.exit("Invalid Input ")


    unit = input("Enter your preferred unit: ").strip().lower()
    if unit != "celsius" and unit != "fahrenheit":
        sys.exit("Invalid unit ")

    try:
        coordinates = lookup(cc)
        if coordinates is None:
            sys.exit("Error ")
        else:
            lat, long = coordinates
            weather_data = weather(lat, long, unit)
    except requests.exceptions.Timeout:
        sys.exit("location service timed out ")
    except requests.exceptions.ConnectionError:
        sys.exit("Unable to find a stable connection")
    except requests.exceptions.HTTPError:
        sys.exit("Error, Unable to reach the servers")
    except requests.exceptions.JSONDecodeError:
        sys.exit("The server returned an invalid response.")
    except ValueError:
        sys.exit('The API returned an unexpected data structure')
    
    
    report = formatting(weather_data, cc, unit)
    print(report)






def lookup(name):#Looksup the place using Geocode api
    splittest = name.split(',')
    splittest_1 = splittest[0].strip()
    splittest_2 = splittest[1].strip()
    place = requests.get('https://geocoding-api.open-meteo.com/v1/search', timeout=10, params={'name': name}) #We request api thru this  
    place.raise_for_status()
    data = place.json()
    if not isinstance(data, dict):
        raise ValueError("Unexpected response ")
    results = data.get("results")
    if not isinstance(results, list):
        raise ValueError("not supported")
    for result in results:
        if splittest_1 == result['name'] and splittest_2 == result['country']:
            lat = result['latitude'] #storing lat
            long = result['longitude'] #storing long
            return lat, long





def weather(latitude, longitude, unit):#Forecast api taking the weather latitude longitude and place
        request = requests.get('https://api.open-meteo.com/v1/forecast', timeout=10, params={'latitude' : latitude, 'longitude' : longitude, 'current' : 'temperature_2m', 'daily' : 'temperature_2m_max,temperature_2m_min', 'forecast_days' : 4, 'temperature_unit' : unit, 'timezone' : 'auto'})
        request.raise_for_status()
        data = request.json()
        if not isinstance(data, dict):
            raise ValueError("Unexpected response")

        current = data.get("current")
        daily = data.get("daily")

        if not isinstance(current, dict) or not isinstance(daily, dict):
            raise ValueError("Unexpected response")

        if "temperature_2m" not in current:
            raise ValueError("Missing current temperature")
        required_daily = ["time", "temperature_2m_max", "temperature_2m_min"]
        if not all(key in daily for key in required_daily):
            raise ValueError("Missing forecast data")

        current_temp = current["temperature_2m"]

        time = daily["time"]
        max_temp = daily["temperature_2m_max"]
        min_temp = daily["temperature_2m_min"]

        if not (len(time) >= 4 and len(max_temp) >= 4 and len(min_temp) >= 4):
            raise ValueError("Incomplete forecast data")

        weather_data = {
    "current_temp": current_temp,
    "dates": time,
    "max_temp": max_temp,
    "min_temp": min_temp
}
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







