from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@sky.pro")
        self.course = Course.objects.create(name="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Test lesson", kurs=self.course, owner=self.user
        )
        # self.client.force_login(user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """Тестирование Course RETRIVE"""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_create(self):
        """Тестирование Course CREATE"""
        url = reverse("materials:course-list")
        data = {"name": "Test course"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        """Тестирование Course UPDATE"""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {"name": "Test course new"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test course new")

    def test_course_delete(self):
        """Тестирование Course DELETE"""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        """Тестирование Course LIST"""
        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lessons": [
                        {
                            "id": self.lesson.pk,
                            "video_url": self.lesson.video_url,
                            "name": self.lesson.name,
                            "description": self.lesson.description,
                            "preview": self.lesson.preview,
                            "kurs": self.course.pk,
                            "owner": self.user.pk,
                        },
                    ],
                    "name": self.course.name,
                    "description": self.course.description,
                    "preview": self.course.preview,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@sky.pro")
        self.course = Course.objects.create(name="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Test lesson", kurs=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирование Lesson RETRIVE"""
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        """Тестирование Lesson CREATE"""
        url = reverse("materials:lesson_create")
        data = {"name": "Test lesson", "kurs": self.course.pk, "owner": self.user.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тестирование Lesson UPDATE"""
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Test lesson new"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test lesson new")

    def test_lesson_delete(self):
        """Тестирование Lesson DELETE"""
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тестирование Lesson LIST"""
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": self.lesson.video_url,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "kurs": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@sky.pro")
        self.course = Course.objects.create(name="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Test lesson", kurs=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """Тестирование Subscription ON"""
        url = reverse("materials:subscription")
        data = {"user": self.user, "course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка добавлена"})

    def test_subscription_delete(self):
        """Тестирование Subscription OFF"""
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        url = reverse("materials:subscription")
        data = {"user": self.user, "course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "Подписка удалена"})
