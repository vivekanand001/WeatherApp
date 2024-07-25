import requests
def forecastweather(lat,lon):
    weatherurl=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=add ur apikey"
    weatherdata=requests.get(weatherurl).json()
    weatherdata={
        "temperature":weatherdata["main"]['temp'],
        "temp_min":weatherdata['main']['temp_min'],
        "temp_max":weatherdata['main']['temp_max'],
        "description":weatherdata['weather'][0]['description'],
        "icon":weatherdata["weather"][0]['icon']
    }
    return weatherdata
