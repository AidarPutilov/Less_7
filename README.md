## Домашняя работа 26.2
- Проект настроен для работы с Celery и celery-beat для выполнения периодических задач.
- Настройки Redis вынесены в переменные окружения.
- Добавлена асинхронная рассылка писем пользователям об обновлении материалов курса.
- Реализована фоновая задача, которая проверяет пользователей по дате последнего входа блокирует их (30 дней).
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
- stripe
- celery
- django-celery-beat
- redis
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
Ввести настройки django, сервера PostgreSQL, платёжной системы Stripe в файле .env.sample. Переименовать файл в .env. При параметре EMAIL_TEST=True рассылка писем не происходит, только сообщение в консоль.
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

#### Запуск обработчика очереди для получения задач и их выполнения
```
celery -A config worker --beat --scheduler django --loglevel=info
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
http://127.0.0.1:8000/users/payment/list/ - Список платежей
http://127.0.0.1:8000/users/payment/create/ - Создание платежа
POST: {"cost": 1000, "method": "cashless", "course": 1}
http://127.0.0.1:8000/users/payment/list?course=<pk> - Фильтрация по курсу
http://127.0.0.1:8000/users/payment/list?lesson=<pk> - Фильтрация по уроку
http://127.0.0.1:8000/users/payment/list?method=cashless - Фильтрация по способу оплаты
http://127.0.0.1:8000/users/payment/list?ordering=date - Сортировка по дате (-date - в обратном порядке)
http://127.0.0.1:8000/users/register/ - Регистрация пользователя
http://127.0.0.1:8000/users/login/ - Получение токена
http://127.0.0.1:8000/users/list/ - Список пользователей
http://127.0.0.1:8000/users/view/<pk>/ - Просмотр пользователя
http://127.0.0.1:8000/users/update/<pk>/ - Редактирование пользователя
http://127.0.0.1:8000/users/delete/<pk>/ - Удаление пользователя
http://127.0.0.1:8000/course/subscription/ - Добаление/удаление подписки
POST: {"course": 1}
```
