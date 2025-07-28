7. MVT Pattern Architecture

Theory:
    
• Django’s MVT (Model-View-Template) architecture and how it handles request-response
cycles.

Ans:-

Django follows the MVT architecture, which stands for:

1)Model – Handles the database. It defines the structure of stored data (tables, fields, relations).

2)View – Contains the business logic. It processes user requests and returns responses.

3)Template – Handles the presentation layer. It’s the HTML part the user sees.

-Request-Response Cycle in Django



1)User Sends Request

-A user types a URL or submits a form.

-The request is sent to the Django server.

2)URL Dispatcher (urls.py)

-Django checks the requested URL.

-It matches the pattern in urls.py and routes the request to the correct View.

3)View Handles Logic (views.py)

-The view function (or class) runs logic.

-It may fetch data using Models.

-It prepares the data to be shown to the user.

4)Model Handles Data (models.py)

-Models interact with the database (read/write data).

-Django ORM helps to access data using Python code.

5)Template Renders Output (templates/)

-The view sends data to a Template.

-The template renders HTML with dynamic data using Django template language.

6)Response to User

-The template returns an HTML response.

-Django sends it back to the user’s browser.



Lab:
    
• Build a simple Django app showcasing how the MVT architecture works

1. Start a Django Project

django-admin startproject student_project
cd student_project
python manage.py startapp studentapp

2. Configure the App

INSTALLED_APPS = [
    ...
    'studentapp',
]

3. Create a Model (M in MVT)

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

Run migrations:

python manage.py makemigrations
python manage.py migrate

4. Create a View (V in MVT)

from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})

5. Create a Template (T in MVT)

<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>
    <h2>All Students</h2>
    <ul>
        {% for student in students %}
            <li>{{ student.name }} - Age: {{ student.age }} - Grade: {{ student.grade }}</li>
        {% empty %}
            <li>No students found.</li>
        {% endfor %}
    </ul>
</body>
</html>

6. Configure URL (URLConf)

from django.contrib import admin
from django.urls import path
from studentapp.views import student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list, name='student-list'),
]

Then run:-

python manage.py runserver


Practical Example:

7) Write a Django project with models, views, and templates to display doctor information.

1. Start a Django Project and App

django-admin startproject hospital_project
cd hospital_project
python manage.py startapp doctorapp

2. Configure the App

INSTALLED_APPS = [
    ...
    'doctorapp',
]

3. Create the Model (Model in MVT)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")

Apply migrations:-

python manage.py makemigrations
python manage.py migrate

4. Create the View (View in MVT)

from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctorapp/doctor_list.html', {'doctors': doctors})

5. Configure URLs

from django.contrib import admin
from django.urls import path
from doctorapp.views import doctor_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', doctor_list, name='doctor-list'),
]

6. Create the Template

<!DOCTYPE html>
<html>
<head>
    <title>Doctor List</title>
</head>
<body>
    <h1>Doctor Information</h1>
    <ul>
        {% for doctor in doctors %}
            <li><strong>{{ doctor.name }}</strong> – {{ doctor.specialty }} ({{ doctor.experience }} years)</li>
        {% empty %}
            <li>No doctor data found.</li>
        {% endfor %}
    </ul>
</body>
</html>

7)Run the Server

python manage.py runserver
