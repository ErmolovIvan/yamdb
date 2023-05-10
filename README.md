# Проект YaMDB
![Github actions](https://github.com/ErmolovIvan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
## Авторы
Проект создан: 

-Ермолов Иван [Ермолов Иван](https://www.youtube.com/watch?v=dQw4w9WgXcQ),

-Башмаков Владислав [Башмаков Владислав](https://www.youtube.com/watch?v=dQw4w9WgXcQ),

-Бессогонова Полина [Бессогонова Полина](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Список технологий

- Django
- Django Rest Framework
- Simple-JWT
- SQLite3
- pytest
- PyJWT
- Nginx
- docker-compose


## Как запустить проект:

Клонировать репозиторий:

```
git clone https://github.com/ErmolovIvan/infra_sp2.git
```

Перейти в папку infra и запустить docker-compose.yaml
(при установленном и запущенном Docker)
```
cd infra_sp2/infra
docker-compose up
```

Для пересборки контейнеров выполнять команду:
(находясь в папке infra, при запущенном Docker)
```
docker-compose up -d --build
```

В контейнере web выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Проверьте работоспособность приложения, для этого перейдите на страницу:

```
 http://localhost/admin/
```

#### С примерами запросов и ответов API можно ознакомиться в документации, после установки и запуска проекта по ссылке: 
```
http://127.0.0.1:8000/redoc/
```

## Примеры запросов
### POST-запрос

```
http://127.0.0.1:8000/api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

### GET-запрос
```
http://127.0.0.1:8000/api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

### DEL-запросы
```
http://127.0.0.1:8000/api/v1/categories/{slug}/
```

### PATCH-запросы
```
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```

```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
