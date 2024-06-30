import requests

TEST_LAT = 41.40338
TEST_LNG = 2.17403

parameters = {
    "lat":TEST_LAT,
    "lng":TEST_LNG,
    "formatted": 1,
}



def get_lat_lng(city="asia/tehran"):
    lat = 35.69439
    lng = 51.42151

    return lat, lng

#response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#response.raise_for_status()


def get_sunset(results):
    sunset = "7:30:27 PM"
    
    return sunset