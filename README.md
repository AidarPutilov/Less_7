## Домашняя работа 24.1
- Добавлено поле вывода количества уроков в сериализатор для модели курса.
- Добавлена модель Платежи.
- Добавлена команда filldb.
- Для сериализатора для модели курса реализовано поле вывода уроков.
- Работа проверена с помощью Postman.
- Чувствительные данные вынесены в переменные окружения и собран шаблон для файла .env.


### Применённые пакеты
- django
- djangorestframework
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
