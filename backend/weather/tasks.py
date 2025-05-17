from celery import shared_task
import requests
from .models import Weather
from datetime import datetime

@shared_task
def fetch_and_store_weather():
    cities = {
        "Taipei": {"lat": 25.05, "lon": 121.53},
        "Taichung": {"lat": 24.15, "lon": 120.67},
        "Kaohsiung": {"lat": 22.63, "lon": 120.30},
    }

    for city, coord in cities.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coord['lat']}&longitude={coord['lon']}&current_weather=true"
        response = requests.get(url)
        data = response.json()

        current = data.get("current_weather", {})
        if current:
            Weather.objects.create(
                city=city,
                temperature=current.get("temperature"),
                windspeed=current.get("windspeed"),
                time=datetime.fromisoformat(current.get("time"))
            )