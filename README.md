create directory.


$mkdir django-puppy-store
$cd django-puppy-store


virtual environment

$python3 -m venv venv
$source venv/bin/activate


install django

$pip3 install django

start project

$django-admin startproject puppy_store

project structure


└── puppy_store
    ├── manage.py
    └── puppy_store
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py


$cd puppy_store

start app

$python3 manage.py startapp puppies

install djangorestframework

pip3 install djangorestframework==3.6.2

add puppies app and rest_framework to INSTALLED_APPS section in settings.py


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    
    'puppies',
]


leave a gap so that you will have idea about apps and packages.

add REST_FRAMEWORK dictionary to settings.py


REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}


install postgresql

$sudo apt-get install postgresql postgresql-contrib

$sudo update-rc.d postgresql enable

$sudo service postgresql start

$sudo -u postgres psql

install psycopg2 to interact with the Postgres server via Python

$pip3 install psycopg2-binary

update DATABASE in setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'puppy_store_drf',
        'USER': '<your-user>',
        'PASSWORD': '<your-password>',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

create the models in models.py

create a database 

$sudo -u postgres psql

$CREATE DATABASE puppy_store_drf;

when done creating models 

$python3 manage.py makemigration

$python3 manage.py migrate

add urls.py to puppies app 

urlpatterns = [
    url(r'^api/v1/puppies/(?P<pk>[0-9]+)$',views.get_delete_update_puppy,name='get_delete_update_puppy'),
    
    url(r'^api/v1/puppies/$',views.get_post_puppies,name='get_post_puppies')
]

add below url to puppy_store/urls.py

    url(r'^', include('puppies.urls')),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework'))
    
create a folder tests under puppies app then add test.py files and __init__.py to initialize the test run

to run the test files 

$python3 manage.py test

ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

with browsable api

http://localhost:8000/api/v1/puppies/

shows list of puppies added to database in json format

http://localhost:8000/api/v1/puppies/<pk>

gives the particular data of primary key

To add values to database throught browsable api 

http://localhost:8000/api/v1/puppies/

Add data in the content field in json format and POST . It will be added to the database

{
    "name": "Muffy",
    "age": 4,
    "breed": "Pamerion",
    "color": "Black"
}

And to update data 

http://localhost:8000/api/v1/puppies/<pk>

with the particular pk value update the values in json format , add it to content field and PUT. It will be updated 