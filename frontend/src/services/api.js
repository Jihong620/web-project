import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const fetchWeatherData = async (params = {}) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/weather-observations/`, {
      params: {
        city: params.city,
        start_date: params.startDate,
        end_date: params.endDate,
        page_size: params.pageSize || 100,
        ordering: params.ordering || '-observed_at'
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching weather data:', error);
    throw error;
  }
};