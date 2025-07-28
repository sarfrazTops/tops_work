6. Project and App Creation


Theory:

    
• Steps to create a Django project and individual apps within the project.

ANS:-

2. Create a Django Project

django-admin startproject project_name


3. Move into the Project Directory

cd project_name


4. Run the Development Server

python manage.py runserver


5. Create an App

python manage.py startapp app_name


6. Add App to Installed Apps

INSTALLED_APPS = [
    ...
    'app_name',
]


7. Define Models

from django.db import models

class Example(models.Model):
    name = models.CharField(max_length=100)

THEN:-

python manage.py makemigrations
python manage.py migrate


8. Create Views and URLs

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from app!")

-In app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


-In project_name/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls')),
]


9. Run the Server Again

python manage.py runserver


• Understanding the role of manage.py, urls.py, and views.py.

ANS:-

1. manage.py – Project Management Script
 
Definition:
    
manage.py is an automatically generated file in every Django project.
It acts as a command-line tool that helps in managing the Django project.

EXAMPLE:-

python manage.py runserver
python manage.py startapp myapp

2. urls.py – URL Routing File

Definition:
    
urls.py is used to define the routing of URLs to specific views.
It controls how web addresses are mapped to view functions.

EXAMPLE:-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

3. views.py – Logic & Response Handler

Definition:
    
views.py is the file where the logic for handling requests and returning responses is written.

EXAMPLE:-

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my site")





Lab:

    
• Create a Django project with an app to manage doctor profiles.

ANS:-

Step 1: Create the Project

django-admin startproject clinic_project
cd clinic_project

Step 2: Create the App

python manage.py startapp doctor

Step 3: Register the App

INSTALLED_APPS = [
    ...
    'doctor',
]


Step 4: Create the Doctor Model

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


Step 5: Make and Apply Migrations

python manage.py makemigrations
python manage.py migrate


Step 6: Create a View to Display Doctors

from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

Step 7: Configure URLs

1.Create doctor/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
]

2.In clinic_project/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctor.urls')),
]

Step 8: Create the Template

<!DOCTYPE html>
<html>
<head>
    <title>Doctor Profiles</title>
</head>
<body>
    <h1>Doctor Profiles</h1>
    <ul>
        {% for doctor in doctors %}
        <li>
            <strong>{{ doctor.name }}</strong> - {{ doctor.specialty }} <br>
            Contact: {{ doctor.phone }} | {{ doctor.email }} <br>
            Bio: {{ doctor.bio }}
        </li>
        <hr>
        {% endfor %}
    </ul>
</body>
</html>


Step 9: Run the Server

python manage.py runserver


Practical Example:

6) Write a Python program to create a Django project and a new app
within the project called doctor.


STEP 2:  create a Django Project 

django-admin startproject clinic_project
cd clinic_project

3: create a Django App (doctor app)

python manage.py startapp doctor


STEP 4: App  settings.py and register

INSTALLED_APPS = [
    ...
    'doctor',  
]

STEP 5: Doctor Model

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


STEP 6: Migrations  (Database setup)


python manage.py makemigrations
python manage.py migrate


STEP 8: Doctor ko admin panel me register karo

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)

STEP 9:  create A View 

from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

STEP 10: URL Setup

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
]

:-clinic_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctor.urls')),
]

STEP 11: CREATE  Template Folder 

<!DOCTYPE html>
<html>
<head>
    <title>Doctor Profiles</title>
</head>
<body>
    <h1>All Doctor Profiles</h1>
    <ul>
        {% for doctor in doctors %}
        <li>
            <strong>{{ doctor.name }}</strong> - {{ doctor.specialty }} <br>
            Contact: {{ doctor.phone }} | {{ doctor.email }} <br>
            Bio: {{ doctor.bio }}
            <hr>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

STEP 12: Then Server Start

python manage.py runserver

