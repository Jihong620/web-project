from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.weather_service import get_weather_summary

@api_view(['GET'])
def get_weather(request):
    data = get_weather_summary()
    return Response(data)
