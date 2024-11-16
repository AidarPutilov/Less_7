from django.db import models

from config.settings import AUTH_USER_MODEL


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
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор курса",
        null=True,
        blank=True,
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
        help_text="Загрузите превью",
        null=True,
        blank=True,
    )
    kurs = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
    )
    video_url = models.CharField(
        max_length=100,
        verbose_name="ссылка на видео",
        help_text="Прикрепите ссылку на видео",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор курса",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["name"]


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"

    def __str__(self):
        return f"{self.user}: {self.course}"
