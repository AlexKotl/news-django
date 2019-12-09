from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def mail(recipient, subject, content):
    return send_mail(subject=subject,
        message=content,
        from_email="",
        recipient_list=[recipient],
        fail_silently=not settings.DEBUG)