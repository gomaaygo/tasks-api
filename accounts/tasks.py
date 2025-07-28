from celery import shared_task

from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        subject='Bem-vindo!',
        message='Obrigado por se cadastrar em nossa API 🎉',
        from_email=None,
        recipient_list=[user_email],
        fail_silently=False,
    )
