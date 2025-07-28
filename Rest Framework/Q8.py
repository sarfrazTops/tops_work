8.Settings Configuration in Django

Theory:
    
•Configuring Django settings for database, static files, and API keys.

Ans:-

In a Django project, configuration settings are managed in the settings.py file.
This file is crucial for defining how the project interacts with databases, handles static
files, and securely manages API keys.

1. Database Configuration

Django supports multiple databases like SQLite, MySQL, and PostgreSQL.
The database settings are defined in the DATABASES dictionary.

Example for SQLite (default):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Example for MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

2. Static Files Configuration

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For deployment

3. API Keys Configuration

API keys (e.g., for Google Maps, Stripe, etc.) should not be hard-coded in settings.py.
Instead, they should be stored securely using environment variables.

Using environment variables:

import os

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

To set the environment variable locally:

export GOOGLE_MAPS_API_KEY='your_real_api_key'

Lab: 
 
•Modify settings.py to connect Django to a MySQL or SQLite database.

ANS:-

Modify settings.py to Connect to SQLite (Default Option)

Django comes pre-configured with SQLite, which is easy to set up and good for small projects.

In settings.py, the DATABASES section looks like this by default:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Modify settings.py to Connect to MySQL
To use MySQL, you must first install the MySQL client:

pip install mysqlclient

Then, modify the DATABASES section in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',    
        'PORT': '3306',
    }
}


After modifying, run migrations to create tables:

python manage.py migrate

Practical Example:

8) Write a Django project that connects to an SQLite database and stores doctor profiles. 

1. Project Setup

django-admin startproject doctor_project
cd doctor_project
python manage.py startapp doctors


2. Configure SQLite in settings.py
SQLite is Django's default database, so no major changes are needed.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Add the app to INSTALLED_APPS:

INSTALLED_APPS = [
    ...
    'doctors',
]

3. Create Doctor Model

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

4. Make Migrations and Migrate

python manage.py makemigrations
python manage.py migrate

5. Register Model in Admin

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)

Create superuser and run the server:

python manage.py createsuperuser
python manage.py runserver
