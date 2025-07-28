18.Live Project Deployment (PythonAnywhere)

Theory: 
 
•Introduction to deploying Django projects to live servers like PythonAnywhere.

Deployment means making your Django project available on the internet so others can access
it using a web browser. One common and beginner-friendly platform for this is PythonAnywhere.

What is PythonAnywhere?
PythonAnywhere is a cloud-based platform that lets you host Python web apps, including Django, without needing to set up your own server.

-Why Use PythonAnywhere?

Free for small apps

Simple to set up

No server maintenance needed

Built-in support for Django

-Steps for Deployment (Overview):
Create an account on pythonanywhere.com

Upload your Django project (via GitHub or ZIP)

Set up a virtual environment

Install dependencies using pip install -r requirements.txt

Deploying to PythonAnywhere allows you to share your Django project live, test it in a
real environment, and learn how web hosting works — an essential skill for every Django
developer.


Lab: 
 
•Deploy a Django project to PythonAnywhere. 

Ans:-

Step 1: Prepare the Django Project Locally

1.Open your Django project on your computer.
2.In settings.py, set the allowed hosts:

ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

3.Create requirements.txt file:

pip freeze > requirements.txt

4.Collect static files:

python manage.py collectstatic

Step 2: Create an Account on PythonAnywhere

1.Go to www.pythonanywhere.com.

2.Sign up and log in.

Step 3: Start a New Web App

1.Click the "Web" tab.

2.Click "Add a new web app".

3.Choose Manual configuration and select your Python version.

Step 4: Upload Your Project
You have two options:

-Option A: Use the "Files" tab to upload your files.

-Option B: Use Git in the "Bash console":

git clone https://github.com/yourusername/yourproject.git

Step 5: Set Up a Virtual Environment
In the Bash console:

cd yourproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Step 6: Configure WSGI File

1.Go to the Web tab.

2.Click on the WSGI configuration file.

3.Add this code at the bottom:

import sys
import os
path = '/home/yourusername/yourproject'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'yourproject.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

Step 7: Set Static Files
In the Web tab, add:

-URL: /static/

-Directory: /home/yourusername/yourproject/static

Step 8: Run Migrations
In the Bash console:

cd yourproject
source venv/bin/activate
python manage.py migrate


Step 9: Reload the Web App

1.Go to the Web tab.

2.Click the Reload button.

-Final Output:

https://yourusername.pythonanywhere.com

Practical Example:
    
18) Write a Django project and deploy it on PythonAnywhere, making it accessible online. 

Part A: Deploy to PythonAnywhere

1. Create a Django Project

django-admin startproject doctorfinder
cd doctorfinder
python manage.py startapp doctors

2. Define Models in doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

3. Register the Model in admin.py

from .models import Doctor
admin.site.register(Doctor)

4. Create Templates (Simple Homepage)
In doctors/views.py:

from django.shortcuts import render
from .models import Doctor

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

-Create templates/home.html:

html
Copy
Edit
<h1>Doctor List</h1>
<ul>
  {% for doc in doctors %}
    <li>{{ doc.name }} - {{ doc.specialty }}</li>
  {% endfor %}
</ul>

5. Add URL Routing
In doctorfinder/urls.py:


from django.contrib import admin
from django.urls import path
from doctors.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

6. Run and Test Locally

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Part B: Deploy to PythonAnywhere

Step 1: Create Account

-Visit https://www.pythonanywhere.com

-Sign up and log in.

Step 2: Upload the Project
Use the Bash console:

git clone https://github.com/yourusername/doctorfinder.git

Step 3: Create Virtual Environment

cd doctorfinder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Step 4: Configure WSGI File
In Web tab > WSGI config file, add:

import sys, os
path = '/home/yourusername/doctorfinder'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'doctorfinder.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

Step 5: Configure Static Files
In the Web tab:

Static URL: /static/

Directory: /home/yourusername/doctorfinder/static

Step 6: Set Environment Variables
In settings.py:

ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

Run:

python manage.py collectstatic
python manage.py migrate

Final Result

https://yourusername.pythonanywhere.com
