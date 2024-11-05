from django.contrib.auth.models import AbstractUser
from django.db import models


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
    # name = models.CharField(
    #     max_length=20,
    #     verbose_name="имя",
    #     help_text="Введите имя",
    #     blank=True,
    #     null=True,
    # )
    # token = models.CharField(
    #     max_length=100,
    #     verbose_name="токен",
    #     blank=True, null=True
    # )
    # is_active = models.BooleanField(
    #     default=True,
    #     verbose_name="активен",
    # )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("name",)

    def __str__(self):
        return self.email
