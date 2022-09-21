import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

celery_app = Celery('app.celery')

celery_app.config_from_object(settings, namespace='CELERY')

@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

celery_app.conf.beat_sechedule = {
    'add-every-24-hour':{
        'task': 'Certificate_Expiration_Verification',
        'schedule': crontab(minute='*/1')
    }
}