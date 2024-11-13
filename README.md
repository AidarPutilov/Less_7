## Домашняя работа 25.1
- Добавлен CRUD для модели User.
- Добавлена команда createusers.
- Добавлена JWT-авторизация.
-
-
- Добавлена модель Платежи.
- Для сериализатора для модели курса реализовано поле вывода уроков.
- Добавлена возможность сортировки по дате.
- Добавлена возможность фильтрации по курсу, уроку и способу оплаты.
- Работа проверена с помощью Postman.
- Чувствительные данные вынесены в переменные окружения и собран шаблон для файла .env.


### Применённые пакеты
- django
- djangorestframework
- djangorestframework-simplejwt
- django-filter
- pillow
- psycopg2-binary
- python-dotenv
- black


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

#### Добавление пользователей и групп
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
### Запросы
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
