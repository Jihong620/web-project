import React from 'react';

const WeatherControls = ({ 
  cities, 
  selectedCity, 
  onCityChange,
  startDate,
  onStartDateChange,
  endDate,
  onEndDateChange,
  onRefresh
}) => {
  return (
    <div className="weather-controls">
      <div className="control-group">
        <label htmlFor="city-select">City:</label>
        <select 
          id="city-select" 
          value={selectedCity} 
          onChange={onCityChange}
        >
          {cities.map(city => (
            <option key={city} value={city}>{city}</option>
          ))}
        </select>
      </div>
      
      <div className="control-group">
        <label htmlFor="start-date">Start Date:</label>
        <input 
          type="date" 
          id="start-date" 
          value={startDate} 
          onChange={onStartDateChange}
        />
      </div>
      
      <div className="control-group">
        <label htmlFor="end-date">End Date:</label>
        <input 
          type="date" 
          id="end-date" 
          value={endDate} 
          onChange={onEndDateChange}
        />
      </div>
      
      <button onClick={onRefresh}>Refresh Data</button>
    </div>
  );
};

export default WeatherControls;