from rest_framework import serializers
from .models import Weather, WeatherObservation

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city', 'temperature', 'windspeed', 'time']

class WeatherObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherObservation
        fields = ['city', 'temperature', 'windspeed', 'observed_at']