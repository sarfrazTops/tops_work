20.SMS Sending APIs (Twilio)

Theory:
    
•Introduction to Twilio API for sending SMS and OTPs.


What is Twilio API?

The Twilio API is a cloud communication platform that allows developers to programmatically
send and receive SMS, MMS, voice calls, WhatsApp messages, and OTP (One-Time Passwords)
through web APIs


Key Features of Twilio API

Send SMS worldwide.

Generate & verify OTPs (via Twilio Verify service).

Two-factor authentication (2FA) integration.

Real-time delivery status tracking.

Works with multiple channels: SMS, Email, Voice, WhatsApp.



How It Works (for SMS/OTP)

Create a Twilio account at https://www.twilio.com/

Get a phone number from Twilio (used as the sender).

Use Twilio’s Python SDK (twilio) to interact with the API.

Send messages or OTPs using verified numbers.



Example: Sending SMS using Python

from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Your OTP is 123456",
    from_='+1415XXXXXXX',  # Twilio number
    to='+91XXXXXXXXXX'     # User's number
)

print(message.sid)

Twilio provides a dedicated Verify API to handle OTP generation and verification securely.

It handles delivery retries, expiration, and rate limits automatically.


Practical Example:

20) Write a Django project that sends an OTP to the user's mobile number during registration
    using Twilio API.

Ans:-

1.Create Project & App

django-admin startproject otp_registration
cd otp_registration
python manage.py startapp otp_app

2.settings.py
Add otp_app to INSTALLED_APPS.

Also add Twilio config (you can move this to .env for safety):


# Twilio config
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1XXXXXXXXXX'     
 
3.forms.py (in otp_app)

from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)

class OTPForm(forms.Form):
    otp = forms.CharField(label="Enter OTP", max_length=6)

4.views.py

Ans:-

from django.shortcuts import render, redirect
from .forms import RegisterForm, OTPForm
from twilio.rest import Client
from django.conf import settings
import random

# Store OTPs temporarily
user_data = {}

def send_otp(phone, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )
    return message.sid

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            otp = str(random.randint(100000, 999999))
            user_data[phone] = {'name': name, 'otp': otp}

            send_otp(phone, otp)
            request.session['phone'] = phone
            return redirect('verify_otp')
    else:
        form = RegisterForm()
    return render(request, 'otp_app/register.html', {'form': form})

def verify_otp(request):
    phone = request.session.get('phone')
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            if phone in user_data and user_data[phone]['otp'] == entered_otp:
                name = user_data[phone]['name']
                del user_data[phone]
                return render(request, 'otp_app/success.html', {'name': name})
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()
    return render(request, 'otp_app/verify_otp.html', {'form': form})


5.URLs
otp_app/urls.py:

python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('verify/', views.verify_otp, name='verify_otp'),
]


otp_registration/urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otp_app.urls')),
]

6.Templates
register.html

<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send OTP</button>
</form>


verify_otp.html


<h2>Enter OTP</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Verify</button>
</form>

Run the Project

python manage.py migrate
python manage.py runserver
