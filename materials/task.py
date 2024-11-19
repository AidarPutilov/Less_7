from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task
def send_info(email):

    print(f'Send mail to {email}')

    # send_mail(
    #     'Новая подписка',
    #     'Новая подписка',
    #     EMAIL_HOST_USER, [email]
    # )
