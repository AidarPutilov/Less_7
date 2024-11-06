## Курсовая работа 6
- Чувствительные данные вынесены в переменные окружения и собран шаблон для файла .env.


### Применённые пакеты
- django
- djangorestframework
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
Ввести настройки django, сервера PostgreSQL в файле .env.sample.
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

#### Запуск проекта
```
python3 manage.py runserver
```
