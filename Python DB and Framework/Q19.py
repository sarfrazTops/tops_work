19.Social Authentication

Theory:
    
•Setting up social login options (Google, Facebook, GitHub) in Django using OAuth2.

Ans:-

To enable social login (Google, Facebook, GitHub) in Django using OAuth2, we typically use
the social-auth-app-django package. OAuth2 is a secure authorization protocol that allows
users to log in using their existing accounts from other platforms without sharing passwords.

1.Install Required Package:

pip install social-auth-app-django

2.Add to settings.py:

INSTALLED_APPS += [
    'social_django',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your-Client-ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your-Client-Secret'

3.Update urls.py:

path('auth/', include('social_django.urls', namespace='social')),


4.Add Login URLs:


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'

5.Create Developer App on:

Google: console.developers.google.com

GitHub: github.com/settings/developers

Facebook: developers.facebook.com

6.Collect Static & Migrate:

python manage.py migrate


Lab: 
 
•Implement Google and Facebook login for the Django project.


Step 1: Install Required Packages

pip install social-auth-app-django

Step 2: Add to settings.py

INSTALLED_APPS += [
    'social_django',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your-Google-Client-ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your-Google-Client-Secret'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'Your-Facebook-App-ID'
SOCIAL_AUTH_FACEBOOK_SECRET = 'Your-Facebook-App-Secret'

# Required middleware
MIDDLEWARE += [
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]


Step 3: Update urls.py

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),  # social login URLs

Step 4: Create Login Buttons in Template (e.g., login.html)

<h2>Login Using</h2>
<a href="{% url 'social:begin' 'google-oauth2' %}">Login with Google</a><br>
<a href="{% url 'social:begin' 'facebook' %}">Login with Facebook</a>


Step 5: Create Apps in Google and Facebook Developer Console
    
Google:
Visit: https://console.developers.google.com

Enable "Google+ API" or "OAuth consent screen"

Add authorized redirect URI:
http://127.0.0.1:8000/auth/complete/google-oauth2/

Facebook:
Visit: https://developers.facebook.com

Add app, configure "Facebook Login"

Redirect URI:
http://127.0.0.1:8000/auth/complete/facebook/

Step 6: Apply Migrations

python manage.py migrate

Step 7: Run the Server

python manage.py runserver


Practical Example:

19) Write a Django project to allow users to log in using Google or Facebook. 
 
Ans:-

Step 1: Create Django Project

django-admin startproject sociallogin_project
cd sociallogin_project
python manage.py startapp users


Step 2: Install Required Package

pip install social-auth-app-django

Step 3: Add Required Settings in settings.py


INSTALLED_APPS += [
    'social_django',
    'users',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE += [
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Google OAuth2 credentials
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your-Google-Client-ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your-Google-Client-Secret'

# Facebook OAuth2 credentials
SOCIAL_AUTH_FACEBOOK_KEY = 'Your-Facebook-App-ID'
SOCIAL_AUTH_FACEBOOK_SECRET = 'Your-Facebook-App-Secret'


Step 4: Update urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('auth/', include('social_django.urls', namespace='social')),
]


Step 5: Create Template home.html

<!DOCTYPE html>
<html>
<head>
    <title>Social Login</title>
</head>
<body>
    <h2>Login with:</h2>
    <a href="{% url 'social:begin' 'google-oauth2' %}">Google</a><br>
    <a href="{% url 'social:begin' 'facebook' %}">Facebook</a>
</body>
</html>


Step 7: Run the Project

python manage.py migrate
python manage.py runserver
