from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # Список пользователей ('эл.адрес', 'название', 'пароль')
        users_list = [
            ("admin@sky.pro", "123"),
            ("user@sky.pro", "123"),
        ]

        # Создание пользователей
        for user_item in users_list:

            # Проверка наличия пользователя, иначе создание
            if not User.objects.filter(email=user_item[0]).exists():
                user = User.objects.create(email=user_item[0])
            else:
                user = User.objects.get(email=user_item[0])

            # Установка параметров
            user.set_password(user_item[1])
            # user.name = user_item[1]
            # user.is_active = True

            # Особые параметры для администратора
            if user_item[1] == "Admin":
                user.is_staff = True
                user.is_superuser = True
            user.save()
