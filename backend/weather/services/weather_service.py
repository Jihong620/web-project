import requests

def get_weather_summary():
    cities = {
        "Taipei": {"lat": 25.05, "lon": 121.53},
        "Taichung": {"lat": 24.15, "lon": 120.67},
        "Kaohsiung": {"lat": 22.63, "lon": 120.30},
    }

    weather_data = []

    for city, coord in cities.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coord['lat']}&longitude={coord['lon']}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        current = data.get("current_weather", {})

        if current:
            weather_data.append({
                "city": city,
                "temperature": current.get("temperature"),
                "windspeed": current.get("windspeed"),
                "time": current.get("time")
            })

    return weather_data
