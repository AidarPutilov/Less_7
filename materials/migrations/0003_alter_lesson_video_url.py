# Generated by Django 5.1.2 on 2024-11-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.CharField(
                blank=True,
                help_text="Прикрепите ссылку на видео",
                max_length=100,
                null=True,
                verbose_name="ссылка на видео",
            ),
        ),
    ]