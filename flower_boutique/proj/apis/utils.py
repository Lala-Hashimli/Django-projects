from django.core.mail import send_mail
from flowers.models import Flowers
from django.conf import settings
from flowers.tasks import send_email_task

def send_email_notification(flower: Flowers):
    send_email_task.delay(flower.id)