# Generated by Django 5.1.2 on 2024-11-10 21:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата платежа"
                    ),
                ),
                (
                    "cost",
                    models.PositiveIntegerField(default=0, verbose_name="стоимость"),
                ),
                (
                    "method",
                    models.CharField(
                        choices=[("cash", "cash"), ("cashless", "cashless")],
                        default="cash",
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="плательщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "оплата",
                "verbose_name_plural": "оплаты",
            },
        ),
    ]
