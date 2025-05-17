import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.worker_pool = 'solo'
app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks(['weather'])

app.conf.timezone = 'Asia/Taipei'
app.conf.beat_schedule = {
    'fetch-weather-every-day': {
        'task': 'weather.tasks.fetch_and_store_weather',
        'schedule': crontab(hour=11, minute=17),
    },
}
