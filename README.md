# Групповой учебный проект: написние REST API для веб-приложения: YaMDb.

## Описание:
Данный сервис собирает отзывы и оценки пользователей на произведения.
Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список категорий может быть расширен администратором.
Пользователи могут оставить текстовый отзыв и оценку произведению, в диапазоне от одного до десяти. Из пользовательских оценок формируется средняя оценка.

Перечень запросов к ресурсу можно посмотреть в описании API после настройки и запуска проекта.
`http://127.0.0.1:8000/redoc/`

## Используемые технологии
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
 
Клонировать репозиторий и перейти в него в командной строке: 
``` 
git clone git@github.com:Epikhin/api_final_yatube.git 
``` 
Cоздать и активировать виртуальное окружение: 
``` 
python3 -m venv env 
``` 
``` 
source env/bin/activate 
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
python manage.py makemigrations 
``` 
``` 
python3 manage.py migrate 
``` 
 
Запустить проект: 
``` 
python3 manage.py runserver 
``` 
Пример использования API: 
 
Для доступа к API необходимо получить токен:  
 
Нужно выполнить POST-запрос localhost:8000/api/v1/token/ передав поля username и password. API вернет JWT-токен 
 
Дальше, передав токен можно будет обращаться к методам, например:  
 
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE) 
 
При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен> 
 
Автор: Епихин Александр 
