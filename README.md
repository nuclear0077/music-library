# music-library

## Technology
Python 3.9, Django 4.1, DRF 3.14, drf-spectacular, SQLite

## Documentation

### Запуск проекта с помощью Docker
```
git clone git@github.com:nuclear0077/music-library.git
```
Перейти в директорию music-library
```
cd music-library
```

Запустим создания образа 
```
docker build . -t docker-music-library   
```

Запустим образ
```
docker run -p 8000:8000 docker-music-library
```

Доступ в админку

http://localhost:8000/admin

login: Test

password: 1

### Документация API.
Для просмотра документации необходимо запустить проект и перейти по ссылке http://localhost:8000/api/schema/swagger-ui/ или http://localhost:8000/api/schema/redoc

### Запуск проекта обычным способом:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:nuclear0077/music-library.git
```

```
cd music-library
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd MusicLibrary
```

```
python3 manage.py migrate
```

Загрузить данные из csv:


Создать супер пользователя:

```
python manage.py createsuperuser
```


Запустить проект:

```
python3 manage.py runserver
```


### Документация API.
Для просмотра документации необходимо запустить проект и перейти по ссылке http://localhost:8000/api/schema/swagger-ui/ или http://localhost:8000/api/schema/redoc



