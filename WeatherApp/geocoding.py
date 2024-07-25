import requests
def geocoding(cityname):
    geour1=f"https://api.geoapify.com/v1/geocode/search?text={cityname}&apiKey=46897ab182d84f9bb348d41997b365c2"
    georesponse=requests.get(geour1).json()
    lat=georesponse["features"][0]["properties"]["lat"]
    lon=georesponse["features"][0]["properties"]["lon"]
    return lat,lon