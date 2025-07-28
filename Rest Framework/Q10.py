10.Social Authentication, Email, and OTP Sending API

Theory: 
 
•Implementing social authentication (e.g., Google, Facebook) in Django.

ocial authentication allows users to log into a Django web application using their existing
accounts from providers like Google or Facebook. This makes the login process faster, more
secure, and user-friendly.

1.OAuth2 Protocol
Social login uses OAuth2, a secure authorization protocol that lets users grant access to their account information without sharing passwords.

2.Third-Party Packages
To simplify integration, developers use libraries like:

social-auth-app-django

django-allauth

1.Install the package:

Update settings.py:

INSTALLED_APPS = [
    ...
    'social_django',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-client-secret'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


3.Add URLs in urls.py:

from django.urls import path, include

urlpatterns = [
    ...
    path('auth/', include('social_django.urls', namespace='social')),
]


Lab: 
 
•Add Google login to a Django project using django-allauth. 

Ans:-

1. Install Required Packages

pip install django-allauth

2. Add to settings.py

INSTALLED_APPS = [
    # Django default apps...
    'django.contrib.sites',

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Redirect URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Optional (for email verification behavior)
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = False


3. Update urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  e
]

4. Run Migrations

python manage.py migrate

5. Add Google App Credentials
Go to: https://console.developers.google.com

Create a project.

Go to OAuth consent screen → configure it.

Go to Credentials → Create Credentials → OAuth Client ID

Select Web application

Add redirect URI: http://localhost:8000/accounts/google/login/callback/



6. Add Social App in Admin Panel

Run the server:

python manage.py runserver


Practical Example:

10) Write a Django project that integrates Google login and sends OTPs to users using Twilio.

Ans:-

1. Install Twilio

pip install twilio

2. Update models.py to store phone numbers



from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)


3. Set Custom User in settings.py

AUTH_USER_MODEL = 'users.CustomUser'

4. Create OTP sending logic



from twilio.rest import Client
import random

def send_otp(phone_number):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    twilio_number = 'your_twilio_phone_number'

    client = Client(account_sid, auth_token)
    otp = random.randint(100000, 999999)
    message = f"Your OTP is: {otp}"

    client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone_number
    )

    return otp


5. Hook into Google Login (Signal or View Override)

# users/signals.py

from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from utils.otp_sender import send_otp

@receiver(user_logged_in)
def send_otp_on_login(request, user, **kwargs):
    if user.phone_number:
        send_otp(user.phone_number)

Then in apps.py:

def ready(self):
    import users.signals

Run migrations:

python manage.py makemigrations
python manage.py migrate

