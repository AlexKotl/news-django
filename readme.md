# News sample
This is a simple news site built with Django, Celery, Poetry and Bootstrap 4.

### Features

- **Bootstrap 4** layout
- **Poetry** dependency manager
- User registration/authentication
- Email validation check using **Mailgun API**
- Create news records with WYSIWYG editor
- News comments
- Sending email notification about new comment using **Celery** with **Redis** broker
- Django admin panel

### Running project
- Install dependencies `poetry install`
- Make sure you set required environment variables, sample could be found in `.env.sample` file
- Start Celery `celery -A news_django worker -l info`
- Start local server `python manage.py runserver`

### Screenshot
![alt text](https://github.com/AlexKotl/news-django/blob/master/static/img/screenshot.png?raw=true) ![alt text](https://github.com/AlexKotl/news-django/blob/master/static/img/screenshot.png?raw=true)