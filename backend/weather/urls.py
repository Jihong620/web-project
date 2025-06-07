from django.urls import path
from .views import get_weather, import_weather_data, get_weather_observations

urlpatterns = [
    path('weather/', get_weather, name='get_weather'),
    path("import-weather/", import_weather_data),
    path('weather-observations/', get_weather_observations)
]