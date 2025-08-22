# flowers/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Flowers
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def check_expired_flowers():
    now = timezone.now()
    product_list = Flowers.objects.filter(status=Flowers.APPROVED, expires_at__lt=now)
    product_list.update(status=Flowers.EXPIRED)

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Flowers

@shared_task
def send_email_task(flower_id):
    flower = Flowers.objects.get(pk=flower_id)
    url = flower.generate_url()  
    send_mail(
        "Subject here",
        f"Your {flower.title} is created. URL: {url}",
        settings.EMAIL_HOST_USER,
        ["2roughjourney4@gmail.com"],
        fail_silently=False,
    )
