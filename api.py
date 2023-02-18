import requests
import json


class OpenWeatherMapApi:
    def __init__(self, api_key: str, lat: float, lon: float, unit: str = "metrics", ):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.unit = unit

    def get_weather(self, exclude: str = ""):
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params={"lat": self.lat, "lon": self.lon, "appid": self.api_key, "units": self.unit, "exclude": exclude})
        json_weather = response.json()
        return json_weather

    def get_current(self, current_option):
        weather = self.get_weather(exclude="minutely,hourly,daily,alerts")
        try:
            if current_option == "weather":
                return weather["current"][current_option][0]["main"]
            else:
                return weather["current"][current_option]

        except KeyError:
            print(f"You gave an invalid key : {current_option}")

