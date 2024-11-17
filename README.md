## Домашняя работа 26.1
- Подключен и настроен вывод документации с помощью drf-yasg.
-

- Добавлен валидатор проверки URL-видео модели Lesson.
- Добавлена модель Subscription и функционал работы подписки.
- В запросе RETRIEVE для Course добавлено поле subscription.
- Реализована пагинация для курсов и уроков.
- Добавлены тесты для CRUD моделей Course и Lesson, функционал работы подписки.
- Работа проверена с помощью Postman.

### Основные приложения
- Python 3.10.12
- Poetry 1.8.2
- git 2.34.1
- VSCode 1.95.2

### Применённые пакеты
- django
- djangorestframework
- djangorestframework-simplejwt
- django-filter
- pillow
- psycopg2-binary
- python-dotenv
- coverage
- drf-yasg
- black

### Пользователи, создаваемые командой createusers:
- admin@sky.pro - Администратор
- mod@sky.pro - Модератор
- user@sky.pro - Владелец всех записей БД

Пароль: 123

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/Less_7.git
```

#### Переход в каталог
```
cd Less_7
```

#### Базовые настройки
```
Ввести настройки django, сервера PostgreSQL в файле .env.sample. Переименовать файл в .env.
```

#### Создание базы данных
```
sudo -i -u postgres
createdb less7
```

#### Активация Poetry, установка пакетов
```
poetry shell
poetry install
```

#### Применение миграций
```
python3 manage.py migrate
```

#### Добавление пользователей и группы Moders
```
python3 manage.py createusers
```

#### Заполнение БД
```
python3 manage.py filldb
```

#### Запуск проекта
```
python3 manage.py runserver
```

#### Запуск тестов
```
python3 manage.py test
```

#### Доступ к документации
```
http://127.0.0.1:8000/swagger/ - Swagger
http://127.0.0.1:8000/redoc/ - Redoc
```

### Запросы
```
http://127.0.0.1:8000/course/ - Список курсов, запрос CREATE
http://127.0.0.1:8000/course/<pk> - Запросы RETRIEVE, PUT, DELETE
http://127.0.0.1:8000/course/lesson/ - Список уроков
http://127.0.0.1:8000/course/lesson/create/ - Создание урока
http://127.0.0.1:8000/course/lesson/<pk>/update/ - Редактирование урока
http://127.0.0.1:8000/course/lesson/<pk>/delete/ - Удаление урока
http://127.0.0.1:8000/users/payment/ - Список платежей
http://127.0.0.1:8000/users/payment?course=<pk> - Фильтрация по курсу
http://127.0.0.1:8000/users/payment?lesson=<pk> - Фильтрация по уроку
http://127.0.0.1:8000/users/payment?method=cashless - Фильтрация по способу оплаты
http://127.0.0.1:8000/users/payment?ordering=date - Сортировка по дате (-date - в обратном порядке)
http://127.0.0.1:8000/users/register/ - Регистрация пользователя
http://127.0.0.1:8000/users/login/ - Получение токена
http://127.0.0.1:8000/users/view/ - Список пользователей
http://127.0.0.1:8000/users/view/<pk>/ - Просмотр пользователя
http://127.0.0.1:8000/users/update/<pk>/ - Редактирование пользователя
http://127.0.0.1:8000/users/delete/<pk>/ - Удаление пользователя
http://127.0.0.1:8000/course/subscription/ - Добаление/удаление подписки
POST: {"course": 1}
```
### Результат проверки покрытия тестами
```
Name                                                                                         Stmts   Miss  Cover
----------------------------------------------------------------------------------------------------------------
config/__init__.py                                                                               0      0   100%
config/asgi.py                                                                                   4      4     0%
config/settings.py                                                                              30      0   100%
config/urls.py                                                                                   3      0   100%
config/wsgi.py                                                                                   4      4     0%
manage.py                                                                                       11      2    82%
materials/__init__.py                                                                            0      0   100%
materials/admin.py                                                                               1      0   100%
materials/apps.py                                                                                4      0   100%
materials/management/__init__.py                                                                 0      0   100%
materials/management/commands/__init__.py                                                        0      0   100%
materials/management/commands/filldb.py                                                         21     21     0%
materials/migrations/0001_initial.py                                                             6      0   100%
materials/migrations/0002_course_owner_lesson_owner.py                                           6      0   100%
materials/migrations/0003_alter_lesson_video_url.py                                              4      0   100%
materials/migrations/0004_subscription.py                                                        6      0   100%
materials/migrations/0005_alter_subscription_options_alter_subscription_course_and_more.py       6      0   100%
materials/migrations/0006_alter_subscription_status.py                                           4      0   100%
materials/migrations/0007_remove_subscription_status.py                                          4      0   100%
materials/migrations/__init__.py                                                                 0      0   100%
materials/models.py                                                                             34      3    91%
materials/paginations.py                                                                         5      0   100%
materials/serializers.py                                                                        29      0   100%
materials/tests.py                                                                             100      0   100%
materials/urls.py                                                                                8      0   100%
materials/validators.py                                                                          5      3    40%
materials/views.py                                                                              68      0   100%
users/__init__.py                                                                                0      0   100%
users/admin.py                                                                                   3      0   100%
users/apps.py                                                                                    4      0   100%
users/management/__init__.py                                                                     0      0   100%
users/management/commands/__init__.py                                                            0      0   100%
users/management/commands/createusers.py                                                        26     26     0%
users/migrations/0001_initial.py                                                                 8      0   100%
users/migrations/0002_alter_user_options_remove_user_username_user_avatar_and_more.py            4      0   100%
users/migrations/0003_payment.py                                                                 6      0   100%
users/migrations/__init__.py                                                                     0      0   100%
users/models.py                                                                                 32      1    97%
users/permissions.py                                                                             9      1    89%
users/serializers.py                                                                            10      0   100%
users/tests.py                                                                                   1      0   100%
users/urls.py                                                                                   10      0   100%
users/views.py                                                                                  33      3    91%
----------------------------------------------------------------------------------------------------------------
TOTAL                                                                                          509     68    87%
```