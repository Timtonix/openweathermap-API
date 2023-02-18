"""
Etant donné (Given)
Lorsque (When)
Alors (Then)
"""
import pytest
from api import OpenWeatherMapApi


@pytest.fixture(scope="session")
def api_obj():
    obj = OpenWeatherMapApi("45c7cef18d074acb6f50f563fd6a6f9f", 48.208176, 16.373)
    return obj


def test_invalid_credentials():
    obj = OpenWeatherMapApi("4dfgezerfv", 48.208176, 16.373)
    weather = obj.get_weather()
    assert weather['cod'] == 401


def test_type_get_weather(api_obj):
    weather = api_obj.get_weather()
    assert type(weather) == dict
    assert weather["lat"] == round(api_obj.lat, 4)


@pytest.mark.parametrize("current,current_type", [("dt", int), ("temp", float), ("humidity", int)])
def test_get_current(api_obj, current, current_type):
    current = api_obj.get_current(current)
    assert type(current) == current_type

def test_get_current_weather(api_obj):
    current_cloud = api_obj.get_current("weather")
    assert type(current_cloud) == str

def test_get_current_invalid_param(api_obj):
    current = api_obj.get_current("bird")
    pytest.raises(KeyError)
