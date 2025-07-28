Module 16) Python DB and Framework


1. HTML in Python

Theory:

• Introduction to embedding HTML within Python using web frameworks like Django or Flask

Modern web development often involves combining HTML (the structure of the web page)
with Python (backend logic). Python web frameworks such as Django and Flask provide ways to
embed HTML within Python projects using templates.

1. What is HTML Embedding in Web Frameworks?

Embedding HTML means creating web pages with HTML that can dynamically display data from
Python. This is typically done using template engines, which allow you to insert Python-like
code into HTML files.

2. Using Templates:
Both Flask and Django use template engines:

Flask uses Jinja2.

Django uses its own templating language (similar to Jinja2).

Templates use placeholders, conditions, and loops to render content dynamically.


• Generating dynamic HTML content using Django templates.

In Django, dynamic HTML content is generated using its template engine, which allows Python
data to be inserted into HTML files. This system separates the backend logic (Python)
from the frontend (HTML), ensuring cleaner, more maintainable code.

<!DOCTYPE html>
<html>
<body>
  <h1>Hello, {{ name }}!</h1>
  <ul>
    {% for subject in subjects %}
      <li>{{ subject }}</li>
    {% endfor %}
  </ul>
</body>
</html>


Lab:

• Write a Python program to render an HTML file using Django’s template system.

1. Create the Django Project and App

Run these commands:

django-admin startproject myproject
cd myproject
python manage.py startapp myapp

2. views.py (in myapp/)

from django.shortcuts import render

def home(request):
    context = {'name': 'Alice'}
    return render(request, 'home.html', context)

3. home.html (in myapp/templates/)
Create a folder: myapp/templates/ and then this file inside:

<!-- home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Django Template</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
</body>
</html>

4. urls.py (in myapp/)
Create a new file named urls.py if it doesn’t exist:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

5. Connect App URLs in myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

6. Add App to Settings in myproject/settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]


Also make sure this is set:
    
import os
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR,/'templates'],
        ...
    },
]

-Run the Server:
     
python manage.py runserver



Practical Example:

    
1. Write a Django project that renders an HTML file displaying “Welcome to Doctor Finder” on
the home page.



Practical Example:

  
1. Write a Django project that renders an HTML file displaying “Welcome to Doctor Finder” on
the home page.


First:-

-Create a new Django project:
django-admin startproject doctor_finder

-Navigate into your project folder:
cd doctor_finder

Create a new Django app:
-python manage.py startapp home


-Register the app in your project:

INSTALLED_APPS = [
    ...
    'home',
]


-Then create template folder wihtin folder wrrite the code

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Finder</title>
</head>
<body>
    <h1>Welcome to Doctor Finder</h1>
</body>
</html>


. Set up the view to render the HTML page:

from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')


. Configure the URL for the homepage:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


-Now, link the app's URLs to the main project's urls.py file (doctor_finder/urls.py):

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

Run the server:

python manage.py runserver







