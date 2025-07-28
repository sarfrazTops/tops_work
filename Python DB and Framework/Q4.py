4. Django Introduction


Theory:
    
• Overview of Django: Web development framework.

Overview of Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.

It follows the Model-View-Template (MVT) architectural pattern.

Django is designed to help developers take applications from concept to completion as quickly as possible.

It emphasizes reusability, less code, rapid development, and follows the DRY (Don't Repeat Yourself) principle.

Comes with built-in features like:

Admin interface

Authentication system

ORM (Object Relational Mapping) for database interaction

URL routing

Form handling

Security features (e.g., protection against CSRF, XSS, SQL injection)

Django is suitable for both small projects and large-scale web applications.


• Advantages of Django (e.g.,scalability, security).
                                                                              
Advantages of Django
                                                                              
Scalability

Django can handle high traffic and large volumes of data.

Used by big websites like Instagram and Pinterest.

Security

Built-in protection against common attacks like SQL injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).

Manages user authentication securely.

Rapid Development

Developers can build and launch applications quickly.

Includes ready-to-use features like admin panel, authentication, etc.

Built-in Admin Interface

Auto-generated admin panel for managing data models.

Versatile

Suitable for any type of web app: content management systems, e-commerce sites, social networks, APIs, etc.

DRY Principle (Don’t Repeat Yourself)

Encourages reusable and maintainable code.

Large Community & Documentation

Extensive documentation and active community support.

ORM (Object-Relational Mapping)

Easy interaction with databases using Python instead of SQL.










• Django vs. Flask comparison:
                                                                              
Django (Full-Stack Framework)
Full-Featured Framework

Comes with built-in tools: admin panel, authentication, ORM, security, etc.

Follows MVT Pattern

Model-View-Template architecture for structured development.

Rapid Development

Ideal for building large applications quickly with less coding.

Built-in Admin Interface

Auto-generated backend for managing data models.

Secure by Default

Protection against CSRF, SQL Injection, XSS, etc.

ORM Support

Built-in Object Relational Mapping (ORM) for easy database interaction.

Less Flexibility, More Convention

You follow Django's way of doing things (pre-defined structure).

Best For:

Big applications, e-commerce, social media platforms, CMS, etc.





Flask (Micro Framework)
Lightweight & Minimal

Basic framework that gives you the tools to build as you like.

Flexible Structure

You design your own architecture — more freedom for custom apps.

No Built-in Admin or ORM

Add features manually using third-party extensions.

Easy to Learn

Simpler for beginners and small projects.

Ideal for APIs and Microservices

Perfect for RESTful APIs, lightweight apps, or prototype projects.

Explicit Code Structure

You control every part, which is great for small teams or specific needs.

Extensible

Easily add features using extensions (e.g., Flask-SQLAlchemy, Flask-Login).

Best For:

Small apps, REST APIs, or apps where you need full control over everything.


Lab:
                                                                              
• Write a short project using Django’s built-in tools to render a simple webpage.

1. Create a Django Project
                                                                              
django-admin startproject mysite
cd mysite

2. Create a Django App

python manage.py startapp homepage


3. Register the App

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'homepage',
]

4. Create a URL in App

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


5. Create a View                                                                              
                                                                              
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')


6. Set up Template

<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Welcome to My Django Website!</h1>
</body>
</html>


7. Run the Server

python manage.py runserver


Practical Example:

4) Write a Python program to create a Django project and understand its
directory structure.





