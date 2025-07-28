9. URL Patterns and Template Integration

Theory:
    
• Setting up URL patterns in urls.py for routing requests to views.

In Django, the urls.py file is used to map URLs (requested by the user) to the corresponding
view functions. This is known as URL routing.

Django uses this routing system to decide what response to send when a user visits a certain
URL in the browser.

Django uses urls.py to match user-requested paths to view functions. This enables smooth
navigation and separation of logic across the app.


• Integrating templates with views to render dynamic HTML content.

A template in Django is an HTML file used to display dynamic content.
Django uses its own template language to embed variables, loops, and conditions into HTML.

Integrating templates with views allows Django to render dynamic HTML pages by passing data
from Python views to HTML templates using context variables.


Lab:
    
• Create a Django project with URL patterns and corresponding views and templates.

1. Create Project and App

django-admin startproject hospital_project
cd hospital_project
python manage.py startapp doctorapp

2. Configure the App

INSTALLED_APPS = [
    ...
    'doctorapp',
]

3. Create Sample View

from django.shortcuts import render

def doctor_list(request):
    doctors = [
        {"name": "Dr. Asha", "specialty": "Cardiologist"},
        {"name": "Dr. Rahul", "specialty": "Dermatologist"},
    ]
    return render(request, 'doctorapp/doctor_list.html', {'doctors': doctors})

4. Create URL Patterns

from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor-list'),
]

5. Create Template

<!DOCTYPE html>
<html>
<head>
    <title>Doctor List</title>
</head>
<body>
    <h1>Available Doctors</h1>
    <ul>
        {% for doctor in doctors %}
            <li>{{ doctor.name }} - {{ doctor.specialty }}</li>
        {% empty %}
            <li>No doctors available.</li>
        {% endfor %}
    </ul>
</body>
</html>

6. Run the Server

python manage.py runserver


Practical Example:

9) Write a Django project where URL routing is used to navigate
between different pages of a “Doctor Finder” site (home, profile, contact)

1. Create Project and App

django-admin startproject doctorfinder
cd doctorfinder
python manage.py startapp main

2. Register the App

INSTALLED_APPS = [
    ...
    'main',
]

4. Create Views

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def profile(request):
    doctor = {
        'name': 'Dr. Neha Sharma',
        'specialty': 'Cardiologist',
        'experience': 10,
    }
    return render(request, 'main/profile.html', {'doctor': doctor})

def contact(request):
    return render(request, 'main/contact.html')

5. Create URL Routing

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
]

B. Project-level URLs: doctorfinder/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include app URLs
]

6. Create HTML Templates

<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    <h1>Welcome to Doctor Finder</h1>
    <a href="{% url 'profile' %}">Doctor Profile</a> |
    <a href="{% url 'contact' %}">Contact Us</a>
</body>
</html>

profile.html

<!DOCTYPE html>
<html>
<head><title>Doctor Profile</title></head>
<body>
    <h2>Doctor Profile</h2>
    <p><strong>Name:</strong> {{ doctor.name }}</p>
    <p><strong>Specialty:</strong> {{ doctor.specialty }}</p>
    <p><strong>Experience:</strong> {{ doctor.experience }} years</p>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>

contact.html

<!DOCTYPE html>
<html>
<head><title>Contact</title></head>
<body>
    <h2>Contact Us</h2>
    <p>Email: info@doctorfinder.com</p>
    <p>Phone: +91-9876543210</p>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>

7. Run the Server

python manage.py runserver
