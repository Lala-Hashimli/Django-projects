# proj/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulunu göstər
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# settings-dəki Celery konfiqurasiyasını yüklə
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django app-lərindən task-ları avtomatik aşkar et
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'flowers.tasks.check_expired_flowers',
        'schedule': 5
    },
}
app.conf.timezone = 'Asia/Baku'