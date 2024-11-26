from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from config.settings import EMAIL_HOST_USER, EMAIL_TEST
from datetime import timedelta, date, datetime

from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_info(course_id):
    """Отправка писем подписчикам курса при обновлении."""

    course = Course.objects.get(pk=course_id)
    items = Subscription.objects.filter(course=course_id)
    emails = [item.user.email for item in items]
    if EMAIL_TEST:
        print(f"Test: Send mail to {emails}: {course} updated")
    else:
        if not emails:
            print(f"Send mail to {emails}")
            send_mail(
                "Курс обновился", f"Курс {course} обновился", EMAIL_HOST_USER, emails
            )
        else:
            print("No send email: no subscribers")


@shared_task
def check_inactive_users():
    """Блокировка неактивных пользователей (>30 дней). Запуск раз в сутки."""

    today = timezone.now().today()
    print(today.date())
    users = User.objects.filter(
        is_active=True, is_staff=False, is_superuser=False, last_login__isnull=False
    )
    date_delta = timedelta(30)
    for user in users:
        date_block = today - date_delta
        if user.last_login <= date_block:
            print(f"User {user} is inactive, blocked")
            user.is_active = False
            user.save()
