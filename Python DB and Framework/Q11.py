11. Django Database Connectivity (MySQL or SQLite)

Theory:
    
• Connecting Django to a database (SQLite or MySQL).

1. Using SQLite (Default)

SQLite is a lightweight, file-based database.

It is the default database in Django and perfect for small projects or beginners.

No need to install anything extra.

-Settings (in settings.py):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Django automatically creates a db.sqlite3 file in our project directory.

2. Using MySQL (External Database)

-MySQL is used for larger, production-level applications.

-Requires:

-MySQL server installed

-Python connector: mysqlclient (or PyMySQL)

:-Installation:

pip install mysqlclient


Settings (in settings.py):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

3. Apply Migrations

python manage.py makemigrations
python manage.py migrate


• Using the Django ORM for database queries.

Using the Django ORM (Object-Relational Mapping) for Database Queries
Django provides a powerful feature called ORM (Object-Relational Mapping)
that allows developers to interact with the database using Python code instead of
writing raw SQL queries.

ORM connects your Django models to database tables, making it easier to perform CRUD
operations (Create, Read, Update, Delete).

Lab:
    
• Set up database connectivity for a Django project.

Ans:-

Step 1: Create a Django Project

django-admin startproject myproject
cd myproject


Step 2: Open settings.py File
Locate the DATABASES dictionary in the settings.py file of your project. This file is located inside the project folder (e.g., myproject/settings.py).

Django comes with SQLite configured by default. The settings look like this:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


B. For MySQL Database:
To use MySQL instead of SQLite, 

🔹 1. Install MySQL Client
Install the MySQL connector using pip:

pip install mysqlclient


🔹 2. Create a Database in MySQL

CREATE DATABASE mydatabase;

🔹 3. Update settings.py for MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


Step 3: Run Migrations

python manage.py makemigrations
python manage.py migrate







