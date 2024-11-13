from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание пользователей и групп."""

    def handle(self, *args, **kwargs):

        # Список групп [('название', ('пользователи',))]
        groups_list = [
            (
                "Moders",
                (
                    "mod@sky.pro",
                ),
            )
        ]

        # Создание групп
        for group_item in groups_list:
            if not Group.objects.filter(name=group_item[0]).exists():
                Group.objects.create(name=group_item[0])
            else:
                Group.objects.get(name=group_item[0])

        # Список пользователей ('эл.адрес', 'название', 'пароль')
        users_list = [
            ("admin@sky.pro", "123"),
            ("mod@sky.pro", "123"),
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
            user.is_active = True

            # Особые параметры для администратора
            if user_item[0] == "admin@sky.pro":
                user.is_staff = True
                user.is_superuser = True
            user.save()

        # Добавление пользователей в группы
        for group_item in groups_list:
            group = Group.objects.get(name=group_item[0])
            for user_item in group_item[1]:
                user = User.objects.get(email=user_item)
                user.groups.add(group)
