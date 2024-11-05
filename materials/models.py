from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="название курса",
        help_text="Введите название",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="описание курса",
        help_text="Введите описание",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="preview/course/",
        verbose_name="превью курса",
        null=True,
        blank=True,
        help_text="Загрузите превью",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["name"]


class Lesson(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="название урока",
        help_text="Введите название",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="описание урока",
        help_text="Введите описание",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="preview/lesson/",
        verbose_name="превью урока",
        null=True,
        blank=True,
        help_text="Загрузите превью",
    )
    kurs = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
    )
    video_url = models.TextField(
        verbose_name='ссылка на видео',
        help_text="Прикрепите ссылку на видео",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["name"]
