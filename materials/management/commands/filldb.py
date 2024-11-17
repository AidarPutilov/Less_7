from django.core.management import BaseCommand
from materials.models import Lesson, Course
from users.models import User, Payment


class Command(BaseCommand):
    """Заполнение Базы данных."""

    def handle(self, *args, **kwargs):

        # Владелец данных
        user = User.objects.get(email="user@sky.pro")

        # Курсы
        course1 = Course.objects.create(
            name="Начальная школа", description="Начальная школа", owner=user
        )
        course2 = Course.objects.create(
            name="Средняя школа", description="Средняя школа", owner=user
        )

        # Уроки
        Lesson.objects.create(
            name="Арифметика", description="Математика", kurs=course1, owner=user
        )
        Lesson.objects.create(
            name="Правописание", description="Русский язык", kurs=course1, owner=user
        )
        Lesson.objects.create(
            name="Граматика", description="Русский язык", kurs=course1, owner=user
        )
        lesson4 = Lesson.objects.create(
            name="Алгебра", description="Математика", kurs=course2, owner=user
        )
        lesson5 = Lesson.objects.create(
            name="Геометрия", description="Математика", kurs=course2, owner=user
        )
        lesson6 = Lesson.objects.create(
            name="Теормеханика", description="Физика", kurs=course2, owner=user
        )
        lesson7 = Lesson.objects.create(
            name="Неорг. химия", description="Химия", kurs=course2, owner=user
        )

        # Платежи
        Payment.objects.create(
            user=user,
            date="2024-08-30",
            course=course1,
            cost=120000,
        )
        Payment.objects.create(
            user=user,
            date="2024-08-30",
            course=course2,
            cost=240000,
        )
        Payment.objects.create(
            user=user,
            date="2024-09-30",
            lesson=lesson4,
            cost=50000,
        )
        Payment.objects.create(
            user=user,
            date="2024-09-30",
            lesson=lesson5,
            cost=40000,
        )
        Payment.objects.create(
            user=user,
            date="2024-09-30",
            lesson=lesson6,
            cost=35000,
            method=Payment.CASHLESS,
        )
        Payment.objects.create(
            user=user,
            date="2024-09-30",
            lesson=lesson7,
            cost=30000,
            method=Payment.CASHLESS,
        )
