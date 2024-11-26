from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson, Subscription
from materials.paginations import CustomPagination
from materials.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
    SubscriptionSerializer,
)
from materials.task import send_info
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """Назначение владельца курса."""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        """Оправка писем при обновлении курса."""
        # print("1")
        course = serializer.save()
        # print("2")
        course_pk = self.get_object().pk
        send_info.delay(course_pk)
        course.save()

    def get_permissions(self):
        """Назначение разрешений."""
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        """Назначение владельца курса"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner, IsAuthenticated | ~IsModer)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModer | IsOwner, IsAuthenticated)


class SubscriptionAPIView(APIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            # Удаление подписки
            subs_item.delete()
            message = "Подписка удалена"
        else:
            # Создание подписки
            Subscription.objects.create(user=user, course=course)
            message = "Подписка добавлена"
        return Response({"message": message})


# Need fix
# https://my.sky.pro/student-cabinet/stream-lesson/119727/homework-requirements
# 8:32
