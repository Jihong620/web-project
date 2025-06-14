import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const fetchWeatherData = async (params = {}) => {
  try {
    // 輸入 API URL 與請求參數
    const response = await axios.get(`${API_BASE_URL}/weather-observations/`, {
      params: {
        city: params.city, // 指定城市
        start_date: params.startDate, // 起始日期
        end_date: params.endDate,  // 結束日期
        page_size: params.pageSize || 100, // 每頁數據量，預設 100 筆
        ordering: params.ordering || '-observed_at' // 排序
      }
    });
    return response.data;
   // 錯誤處理
  } catch (error) {
    console.error('Error fetching weather data:', error);
    throw error;
  }
};