from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    windspeed = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.city} - {self.time}"

    class Meta:
        db_table = 'weather_data'  # Table 名稱

class ForecastData(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=100)
    forecast_date = models.DateField()
    temperature_high = models.FloatField()
    temperature_low = models.FloatField()
    windspeed = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False # 告訴 Django : 這張表格不需要管理
        db_table = 'forecast_data'