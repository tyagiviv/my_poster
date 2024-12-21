Read me:
- create local project folder
- create reporsitory in github
- create connection between your local folder and github repository


- install django: 
  - python -m pip install django==3.0.10

- start project:
  - django-admin startproject <name of your project> .
  - it will create project in your local prj folder 

- Run your servers
  - python manage.py runserver
  - it will start your server

- start your app
  - python manage.py startapp <name of your app>
  - it will create app folder in your local prj folder
  - add your app name in settings under INSTALLED_APPS

- create models in models.py:

- make migrations:
  - python manage.py makemigrations
  - python manage.py migrate

- can create table and data if necessary

- now can create views and path in 
  - views.py &
  - urls.py
