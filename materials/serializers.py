from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    # courses = serializers.SerializerMethodField()

    # def get_courses(self, lesson):
    #     return [course.name for course in Course.objects.filter(lesson=lesson)]

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    def get_lesson_count(self, course):
        return Lesson.objects.filter(kurs=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "lessons", "lesson_count")
