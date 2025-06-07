import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
} from 'chart.js';
import 'chartjs-adapter-date-fns';

// 註冊 Chart.js 組件
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
);

const WeatherChart = ({ data, city }) => {
  // 過濾當前城市數據並按時間排序
  const cityData = data
    .filter(item => item.city === city)
    .sort((a, b) => new Date(a.observed_at) - new Date(b.observed_at));

  // 準備圖表數據
  const chartData = {
    datasets: [
      {
        label: `${city} 溫度 (°C)`,
        data: cityData.map(item => ({
          x: item.observed_at,
          y: item.temperature
        })),
        borderColor: 'rgba(255, 99, 132, 0.8)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderWidth: 2,
        tension: 0.1,
        yAxisID: 'y',
      },
      {
        label: `${city} 風速 (km/h)`,
        data: cityData.map(item => ({
          x: item.observed_at,
          y: item.windspeed
        })),
        borderColor: 'rgba(53, 162, 235, 0.8)',
        backgroundColor: 'rgba(53, 162, 235, 0.2)',
        borderWidth: 2,
        tension: 0.1,
        yAxisID: 'y1',
      }
    ]
  };

  const options = {
    responsive: true,
    interaction: {
      intersect: false,
      mode: 'index',
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: (context) => {
            let label = context.dataset.label || '';
            if (label) {
              label += ': ';
            }
            label += context.parsed.y.toFixed(1);
            return label;
          }
        }
      },
    },
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'day',
          displayFormats: {
            hour: 'MM/dd HH:mm',
            day: 'MM/dd'
          }
        },
        title: {
          display: true,
          text: '觀測時間'
        }
      },
      y: {
        title: {
          display: true,
          text: '溫度 (°C)'
        },
      },
      y1: {
        position: 'right',
        title: {
          display: true,
          text: '風速 (km/h)'
        },
        grid: {
          drawOnChartArea: false,
        },
      },
    },
  };

  return (
    <div style={{ position: 'relative', height: '500px', width: '100%' }}>
      <Line 
        options={options} 
        data={chartData} 
      />
    </div>
  );
};

export default WeatherChart;