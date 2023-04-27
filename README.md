# api_final
api_final_yatube - это API для проекта Yatube
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/yandex-praktikum/kittygram.git

Cоздать и активировать виртуальное окружение:
python3 -m venv venv
source venv/Scripts/activate

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python manage.py runserver

Примеры. Некоторые примеры запросов к API:
Получение публикаций:
http://127.0.0.1:8000/api/v1/posts/

Получение публикации:
http://127.0.0.1:8000/api/v1/posts/{id}/

Создание публикации:
http://127.0.0.1:8000/api/v1/posts/

{
  "text": "string",
  "image": "string",
  "group": 0
}

Обновление публикации:
http://127.0.0.1:8000/api/v1/posts/{id}/

{
  "text": "string",
  "image": "string",
  "group": 0
}

Частичное обновление публикации:
http://127.0.0.1:8000/api/v1/posts/{id}/

{
  "text": "string",
  "image": "string",
  "group": 0
}

Удаление публикации:
http://127.0.0.1:8000/api/v1/posts/{id}/

Получение комментариев:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Добавление комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

{
  "text": "string"
}

Получение комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Обновление комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

{
  "text": "string"
}

Частичное обновление комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

{
  "text": "string"
}

Удаление комментария:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Список сообществ:
http://127.0.0.1:8000/api/v1/groups/

Информация о сообществе:
http://127.0.0.1:8000/api/v1/groups/{id}/

Подписки:
http://127.0.0.1:8000/api/v1/follow/

Подписка:
http://127.0.0.1:8000/api/v1/follow/

{
  "following": "string"
}

Получить JWT-токен:
http://127.0.0.1:8000/api/v1/jwt/create/

{
  "username": "string",
  "password": "string"
}

Обновить JWT-токен:
http://127.0.0.1:8000/api/v1/jwt/refresh/

{
  "refresh": "string"
}

Проверить JWT-токен:
http://127.0.0.1:8000/api/v1/jwt/verify/

{
  "token": "string"
}