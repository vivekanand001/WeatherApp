import requests
def geocoding(cityname):
    geour1=f"https://api.geoapify.com/v1/geocode/search?text={cityname}&apiKey=add ur apikey"
    georesponse=requests.get(geour1).json()
    lat=georesponse["features"][0]["properties"]["lat"]
    lon=georesponse["features"][0]["properties"]["lon"]
    return lat,lon
