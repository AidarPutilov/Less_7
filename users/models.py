from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите Email",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="телефон",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=20,
        verbose_name="город",
        help_text="Введите город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        verbose_name="аватар",
        null=True,
        blank=True,
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("email",)

    def __str__(self):
        return self.email


class Payment(models.Model):
    CASH = "cash"
    CASHLESS = "cashless"
    PAYMENT_METHOD = [(CASH, "cash"), (CASHLESS, "cashless")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="плательщик")
    date = models.DateField(
        verbose_name="дата платежа",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс",
        null=True,
        blank=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="урок",
        null=True,
        blank=True,
    )
    cost = models.PositiveIntegerField(default=0, verbose_name="стоимость")
    method = models.CharField(
        choices=PAYMENT_METHOD, default=CASH, verbose_name="способ оплаты"
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        null=True,
        blank=True,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="ссылка на оплату",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        verbose_name="статус платежа",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "платёж"
        verbose_name_plural = "платежи"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user}: {self.cost}"
