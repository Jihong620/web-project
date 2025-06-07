import React, { useState, useEffect } from 'react';
import WeatherChart from '../components/WeatherChart';
import WeatherControls from '../components/WeatherControls';
import { fetchWeatherData } from '../services/api';

const WeatherPage = () => {
  const [weatherData, setWeatherData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedCity, setSelectedCity] = useState('Taipei');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const cities = ['Taipei', 'Taichung'];

  useEffect(() => {
    const today = new Date();
    const defaultEndDate = today.toISOString().split('T')[0];
    const defaultStartDate = new Date(today.setDate(today.getDate() - 7)).toISOString().split('T')[0];

    setStartDate(defaultStartDate);
    setEndDate(defaultEndDate);
  }, []);

  useEffect(() => {
    if (startDate && endDate) {
      fetchData(selectedCity, startDate, endDate);
    }
  }, [selectedCity, startDate, endDate]);

  const fetchData = async (city, start, end) => {
    setLoading(true);
    setError(null);
    try {
      console.log("📤 發送 API 前的參數：", { city, start, end });

      const data = await fetchWeatherData({
        city,
        startDate: start,
        endDate: end
      });

      console.log("📥 從後端取得的資料：", data);

      setWeatherData(data.results);
    } catch (err) {
      setError('Failed to fetch weather data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCityChange = (e) => {
    const city = e.target.value;
    setSelectedCity(city);
    fetchData(city, startDate, endDate);
  };

  const handleStartDateChange = (e) => {
    const date = e.target.value;
    setStartDate(date);
  };

  const handleEndDateChange = (e) => {
    const date = e.target.value;
    setEndDate(date);
  };

  const handleRefresh = () => {
    fetchData(selectedCity, startDate, endDate);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="weather-page">
      <h1>Weather Trends</h1>
      
      <WeatherControls
        cities={cities}
        selectedCity={selectedCity}
        onCityChange={handleCityChange}
        startDate={startDate}
        onStartDateChange={handleStartDateChange}
        endDate={endDate}
        onEndDateChange={handleEndDateChange}
        onRefresh={handleRefresh}
      />
      
      <div className="chart-container">
        <WeatherChart data={weatherData} city={selectedCity} />
      </div>
    </div>
  );
};

export default WeatherPage;