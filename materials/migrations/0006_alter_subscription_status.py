# Generated by Django 5.1.2 on 2024-11-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "materials",
            "0005_alter_subscription_options_alter_subscription_course_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="status",
            field=models.BooleanField(default=True, verbose_name="статус подписки"),
        ),
    ]
