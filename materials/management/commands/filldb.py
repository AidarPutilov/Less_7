from django.core.management import BaseCommand
from materials.models import Lesson, Course
from users.models import User, Payment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        course1 = Course.objects.create(
            name="Начальная школа", description="Начальная школа"
        )
        course2 = Course.objects.create(
            name="Средняя школа", description="Средняя школа"
        )

        lesson1 = Lesson.objects.create(
            name="Арифметика", description="Математика", kurs=course1
        )
        lesson2 = Lesson.objects.create(
            name="Правописание", description="Русский язык", kurs=course1
        )
        lesson3 = Lesson.objects.create(
            name="Граматика", description="Русский язык", kurs=course1
        )
        lesson4 = Lesson.objects.create(
            name="Алгебра", description="Математика", kurs=course2
        )
        lesson5 = Lesson.objects.create(
            name="Геометрия", description="Математика", kurs=course2
        )
        lesson6 = Lesson.objects.create(
            name="Теормеханика", description="Физика", kurs=course2
        )
        lesson7 = Lesson.objects.create(
            name="Неорг. химия", description="Химия", kurs=course2
        )

        user1 = User.objects.create(
            email="red@redmail.org", phone="89996677888", city="Москва"
        )
        user2 = User.objects.create(
            email="yellow@yellowmail.org", phone="89992233556", city="Омск"
        )
        user3 = User.objects.create(
            email="green@greenmail.org", phone="89995522777", city="Тверь"
        )

        Payment.objects.create(
            user=user1,
            date="2024-08-30",
            course=course1,
            cost=120000,
        )
        Payment.objects.create(
            user=user2,
            date="2024-08-30",
            course=course2,
            cost=240000,
        )
        Payment.objects.create(
            user=user3,
            date="2024-09-30",
            lesson=lesson4,
            cost=50000,
        )
        Payment.objects.create(
            user=user3,
            date="2024-09-30",
            lesson=lesson5,
            cost=40000,
        )
        Payment.objects.create(
            user=user3,
            date="2024-09-30",
            lesson=lesson6,
            cost=35000,
            method=Payment.CASHLESS,
        )
        Payment.objects.create(
            user=user3,
            date="2024-09-30",
            lesson=lesson7,
            cost=30000,
            method=Payment.CASHLESS,
        )
