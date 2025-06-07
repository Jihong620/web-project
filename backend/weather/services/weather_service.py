import requests
from datetime import datetime, timedelta
import pytz
from django.core.paginator import Paginator, EmptyPage
from ..models import WeatherObservation

CITY_COORDINATES = {
    "Taipei": {"lat": 25.05, "lon": 121.53},
    "Taichung": {"lat": 24.15, "lon": 120.67},
    "Kaohsiung": {"lat": 22.63, "lon": 120.30},
}

def get_weather_summary():
    weather_data = []
    
    for city, coord in CITY_COORDINATES.items():
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

def import_weather_data_from_api(city, start_date, end_date):
    # 參數驗證
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        today = datetime.today().date()
        max_end = today + timedelta(days=15)
        
        if start < today or end > max_end:
            return 0, "Date range must be within next 16 days"
        if city not in CITY_COORDINATES:
            return 0, f"Unsupported city: {city}"
    except ValueError:
        return 0, "Invalid date format (use YYYY-MM-DD)"

    # API 請求與處理
    coord = CITY_COORDINATES[city]
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={coord['lat']}&longitude={coord['lon']}&"
        f"hourly=temperature_2m,windspeed_10m&"
        f"start_date={start_date}&end_date={end_date}&timezone=Asia%2FTaipei"
    )
    
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        
        entries = [
            WeatherObservation(
                city=city,
                temperature=data["hourly"]["temperature_2m"][i],
                windspeed=data["hourly"]["windspeed_10m"][i],
                observed_at=datetime.fromisoformat(t).replace(tzinfo=pytz.UTC)
            )
            for i, t in enumerate(data["hourly"]["time"])
        ]
        
        created_count = len(WeatherObservation.objects.bulk_create(entries, ignore_conflicts=True))
        return created_count, None
        
    except Exception as e:
        return 0, f"Error: {str(e)}"

def get_weather_observation_records(city=None, start_date=None, end_date=None, 
                           ordering='-observed_at', page=1, page_size=10):
    queryset = WeatherObservation.objects.all().order_by(ordering)
    
    # 過濾條件
    if city:
        queryset = queryset.filter(city=city)
    if start_date:
        queryset = queryset.filter(observed_at__date__gte=start_date)
    if end_date:
        queryset = queryset.filter(observed_at__date__lte=end_date)
    
    # 分頁處理
    paginator = Paginator(queryset, page_size)
    try:
        observations = paginator.page(page)
        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': observations.number,
            'results': list(observations)
        }, None
    except EmptyPage:
        return None, "Invalid page number"
    except Exception as e:
        return None, str(e)