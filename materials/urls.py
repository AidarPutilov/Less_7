from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
    LessonUpdateAPIView,
    SubscriptionAPIView,
)
from materials.apps import MaterialsConfig


app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path(
        "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "subscription/",
        SubscriptionAPIView.as_view(),
        name="subscription",
    ),
] + router.urls
