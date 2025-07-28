19.Email Sending APIs (SendGrid, Mailchimp) 
 
Theory: 
 
•Using email sending APIs like SendGrid and Mailchimp to send transactional emails. 

Ans:-

What are Transactional Emails?

Transactional emails are automated, real-time emails sent to a user after specific actions or events. Examples include:

Password reset emails

Order confirmations

Welcome emails


🔌
Why Use Email APIs?
Instead of setting up your own email server (which is complex and unreliable), APIs like SendGrid and Mailchimp Transactional (formerly Mandrill) offer:

Reliable email delivery

High speed and security

Built-in analytics and bounce handling

 Sending a Transactional Email (Example: REST API)
Endpoint:


POST https://api.sendgrid.com/v3/mail/send
Easy integration with Django, Node.js, etc.


Request Headers:

Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

Request Body (JSON):

    {
  "personalizations": [{
    "to": [{ "email": "user@example.com" }],
    "subject": "Welcome to our service!"
  }],
  "from": { "email": "your_email@example.com" },
  "content": [{
    "type": "text/plain",
    "value": "Thank you for signing up."
  }]
}

Lab: 
 
•Implement email sending functionality in a Django project using SendGrid. 

Ans:-

2.Create Project and App

django-admin startproject email_project
cd email_project
python manage.py startapp email_app


3.forms.py (in email_app/)

from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

4.views.py

from django.shortcuts import render
from .forms import EmailForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

# You can use Django-environ or directly load from .env for security
SENDGRID_API_KEY = 'YOUR_SENDGRID_API_KEY'  # Replace this safely in production

def send_email_view(request):
    message = ''
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['message']

            try:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                email = Mail(
                    from_email='your_verified_sender@example.com',
                    to_emails=to_email,
                    subject=subject,
                    plain_text_content=content
                )
                response = sg.send(email)
                if response.status_code == 202:
                    message = 'Email sent successfully!'
                else:
                    message = ' Failed to send email. Try again.'
            except Exception as e:
                message = f'Error: {e}'
    else:
        form = EmailForm()
    return render(request, 'email_app/send_email.html', {'form': form, 'message': message})


5.urls.py (in email_app/)
python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email_view, name='send_email'),
]


6.urls.py (in email_project/)
python
Copy
Edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('email_app.urls')),
]

7.Template: send_email.html

<!DOCTYPE html>
<html>
<head>
    <title>Send Email with SendGrid</title>
</head>
<body>
    <h2>Send Transactional Email</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send Email</button>
    </form>

    {% if message %}
        <p><strong>{{ message }}</strong></p>
    {% endif %}
</body>
</html>


8.Run the Server

python manage.py runserver

 
Practical Example:

19) Write a Django project to send a confirmation email to a user using the SendGrid API
    after successful registration. 

Ans:-

1.Install Django and SendGrid

pip install django sendgrid

2.Create Django Project & App

django-admin startproject user_registration
cd user_registration
python manage.py startapp registration_app

3.settings.py
Add 'registration_app' to INSTALLED_APPS.

python
Copy
Edit
INSTALLED_APPS = [
    ...
    'registration_app',
]

4. forms.py (in registration_app/)
python
Copy
Edit
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')

5.views.py (in registration_app/)

from django.shortcuts import render
from .forms import RegistrationForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your actual SendGrid API Key
SENDGRID_API_KEY = 'YOUR_SENDGRID_API_KEY'
FROM_EMAIL = 'your_verified_sender@example.com'

def register_view(request):
    success_message = ''
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Compose email
            message = Mail(
                from_email=FROM_EMAIL,
                to_emails=email,
                subject='Welcome to Our Site!',
                html_content=f"<p>Hi {name},</p><p>Thanks for registering with us!</p>"
            )

            try:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                response = sg.send(message)
                if response.status_code == 202:
                    success_message = 'Registration successful! Confirmation email sent.'
                else:
                    success_message = '️ Registered, but email failed to send.'
            except Exception as e:
                success_message = f" Error: {str(e)}"
    else:
        form = RegistrationForm()

    return render(request, 'registration_app/register.html', {'form': form, 'message': success_message})


6.urls.py (in registration_app/)

from django.urls import path
from .views import register_view

urlpatterns = [
    path('', register_view, name='register'),
]


7.urls.py (in user_registration/)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration_app.urls')),
]

8.Template: register.html

<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>

    {% if message %}
        <p style="color: green;">{{ message }}</p>
    {% endif %}
</body>
</html>


Run Your Project

python manage.py runserver
