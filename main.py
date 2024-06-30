import requests
import datetime
import json


TEST_LAT = 41.40338
TEST_LNG = 2.17403

parameters = {
    "lat":TEST_LAT,
    "lng":TEST_LNG,
    "formatted": 1,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

if response.status_code == 200:
    data = response.json()

    print(data)

    with open("data.json", mode="w") as data_file:
        data_file.write(str(data))


def get_lat_lng(city="asia/tehran"):
    
    # find the latitude and longitude of a provided city 
    
    lat = 35.69439
    lng = 51.42151

    return lat, lng