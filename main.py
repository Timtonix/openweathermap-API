import api as api

test = api.OpenWeatherMapApi("45c7cef18d074acb6f50f563fd6a6f9f", 48.208176, 16.373)
print(test.get_weather())

print(test.get_current("dt"))