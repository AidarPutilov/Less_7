from rest_framework import serializers
from materials.validators import validate_youtube_link

from materials.models import Course, Lesson, Subscription


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.CharField(
        read_only=True, validators=[validate_youtube_link]
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_lesson_count(self, course):
        """Возвращает количество уроков в курсе"""
        return Lesson.objects.filter(kurs=course).count()

    def get_subscription(self, course):
        """Возвращает наличие подписки на курс"""
        user = self.context["request"].user
        return (
            Subscription.objects.all().filter(user=user).filter(course=course).exists()
        )

    class Meta:
        model = Course
        fields = ("name", "description", "lessons", "lesson_count", "subscription")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
