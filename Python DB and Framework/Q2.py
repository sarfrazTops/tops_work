2. CSS in Python

Theory:
    
• Integrating CSS with Django templates.

In Django, integrating CSS (Cascading Style Sheets) with templates allows you to style your
HTML content, making the webpages visually appealing.
Django follows a modular approach where static files (CSS, JavaScript, images, etc.)
are handled separately from dynamic content.

• How to serve static files (like CSS, JavaScript) in Django

In Django, static files refer to any file that does not change and is directly served to
the user without any dynamic processing, such as CSS, JavaScript, images, fonts, etc.

Django separates dynamic content (such as HTML rendered by templates) from static content
(CSS, JavaScript, images, etc.). The static files are generally stored separately and
are served from specific locations.

Lab:
    
• Create a CSS file to style a basic HTML template in Django.

First

-Create a Django project:

django-admin startproject doctor_finder
cd doctor_finder

-Create a Django app

python manage.py startapp home


-Add the app to INSTALLED_APPS in settings.py:


INSTALLED_APPS = [
    ...
    'home',
]

2. Organizing Static Files

Create the static/css/styles.css file:
    
Inside the static/css/ folder, create a file called styles.css.
This file will contain the CSS styles to style the HTML template.

static/css/styles.css:

/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: blue;
    margin: 0;
    padding: 0;
}

h1 {
    color: black;
    text-align: center;
    margin-top: 50px;
    font-size: 36px;
}

.container {
    width: 80%;
    margin: 0 auto;
    text-align: center;
}

p {
    font-size: 18px;
    color: red;
}

3. Creating the HTML Template

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Finder</title>

    <!-- Link to the CSS file -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>

    <div class="container">
        <h1>Welcome to Doctor Finder</h1>
        <p>Find the best doctors near you easily.</p>
    </div>

</body>
</html>

4. Creating Views and URL Patterns

from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

-Then next:-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

Then Next:-

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
]

5. Running the Server

python manage.py runserver


Practical Example: 2) Write a Django project to display a webpage with custom CSS styling
for a doctor profile page.

1. Project Setup

INSTALLED_APPS = [
    ...
    'profiles',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "profiles" / "static"]


2. URLs

doctor_profile/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
]


profiles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_profile, name='doctor_profile'),
]


3. View

from django.shortcuts import render

def doctor_profile(request):
    context = {
        'name': 'Dr. Sara Khan',
        'specialty': 'Cardiologist',
        'location': 'Ahmedabad, Gujarat',
        'experience': '10 years',
        'about': 'Dr. Sara Khan is a leading cardiologist with over a decade of experience in heart care and surgery.',
    }
    return render(request, 'profiles/doctor_profile.html', context)

4. Template

<!DOCTYPE html>
<html>
<head>
    <title>Doctor Profile</title>
    <link rel="stylesheet" type="text/css" href="{% static 'profiles/style.css' %}">
</head>
<body>
    <div class="profile-container">
        <h1>{{ name }}</h1>
        <h2>{{ specialty }}</h2>
        <p><strong>Location:</strong> {{ location }}</p>
        <p><strong>Experience:</strong> {{ experience }}</p>
        <p class="about">{{ about }}</p>
    </div>
</body>
</html>


5. CSS Styling


body {
    font-family: Arial, sans-serif;
    background-color: #f4f9ff;
    margin: 0;
    padding: 20px;
}

.profile-container {
    background-color: #fff;
    max-width: 600px;
    margin: 0 auto;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.1);
}

.profile-container h1 {
    color: #2c3e50;
    margin-bottom: 10px;
}

.profile-container h2 {
    color: #3498db;
    margin-bottom: 20px;
}

.profile-container p {
    font-size: 16px;
    color: #333;
}

.profile-container .about {
    margin-top: 20px;
    font-style: italic;
}


6. Run the Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver














