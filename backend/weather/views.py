from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import WeatherObservationSerializer
from .services.weather_service import get_weather_summary, import_weather_data_from_api, get_weather_observation_records

@api_view(['GET'])
def get_weather(request):
    data = get_weather_summary()
    return Response(data)

@api_view(['GET'])
def import_weather_data(request):
    city = request.query_params.get("city", "Taipei")
    start_date = request.query_params.get("start")
    end_date = request.query_params.get("end")

    if not (start_date and end_date):
        return Response(
            {"error": "Missing required parameters: 'start' and 'end'"},
            status=status.HTTP_400_BAD_REQUEST
        )

    created_count, error = import_weather_data_from_api(city, start_date, end_date)
    if error:
        status_code = status.HTTP_400_BAD_REQUEST if "Invalid" in error else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response({"error": error}, status=status_code)
    
    return Response({
        "message": f"成功匯入 {created_count} 筆資料",
        "city": city,
        "date_range": f"{start_date} to {end_date}"
    })

@api_view(['GET'])
def get_weather_observations(request):
    params = {
        'city': request.query_params.get('city'),
        'start_date': request.query_params.get('start_date'),
        'end_date': request.query_params.get('end_date'),
        'ordering': request.query_params.get('ordering', '-observed_at'),
        'page': int(request.query_params.get('page', 1)),
        'page_size': int(request.query_params.get('page_size', 10))
    }
    
    result, error = get_weather_observation_records(**params)
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = WeatherObservationSerializer(result['results'], many=True)
    return Response({
        'count': result['count'],
        'total_pages': result['total_pages'],
        'current_page': result['current_page'],
        'results': serializer.data
    })