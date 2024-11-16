## Домашняя работа 25.2
- Добавлен валидатор проверки URL-видео модели Lesson.
- Добавлена модель Subscription и ендпонт для неё.
- В запросе RETRIEVE для Course добавлено поле subscription.
- Реализована пагинация для курсов и уроков.
- 

- Добавлен CRUD для модели User.
- Добавлена команда createusers.
- Добавлена JWT-авторизация.
- Добавлены группа Moders, разрешения для работы с уроками и курсами.
- Добавлены поле owner для курсов и уроков, права доступа для объектов.
- Работа проверена с помощью Postman.

### Применённые пакеты
- django
- djangorestframework
- djangorestframework-simplejwt
- django-filter
- pillow
- psycopg2-binary
- python-dotenv
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