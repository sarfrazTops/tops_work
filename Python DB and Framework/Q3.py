3. JavaScript with Python

Theory:
    
• Using JavaScript for client-side interactivity in Django templates.


Step 1:

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

        <p id="about-short" class="about">
            {{ about|slice:":50" }}...
            <button onclick="toggleAbout()">Show More</button>
        </p>

        <p id="about-full" class="about" style="display:none;">
            {{ about }}
            <button onclick="toggleAbout()">Show Less</button>
        </p>
    </div>

    <script src="{% static 'profiles/script.js' %}"></script> <!-- Optional JS file -->
</body>
</html>



Step 2:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "profiles" / "static"]



Step 3:

python manage.py runserver



• Linking external or internal JavaScript files in Django


1. Place your JS file in the static/ folder of your app.

Example Path:
    
yourapp/static/yourapp/script.js

2 .  Load static files in your template

{% load static %}


3. Link the JS file using <script src="{% static %}">

<script src="{% static 'yourapp/script.js' %}"></script>




Lab:

    
• Create a Django project with JavaScript-enabled form validation.


    
1. Create Django Project & App


django-admin startproject contact_project
cd contact_project
python manage.py startapp contactapp


2. Create Django Form

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


3. Create the View

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    return render(request, 'contactapp/contact.html', {'form': form})


4. URLs Setup

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contactapp.urls')),
]

-contactapp/urls.py

from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', contact_view, name='contact'),
]


5. Create HTML Template with JavaScript

{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <script src="{% static 'contactapp/script.js' %}"></script>
    <style>
        form { max-width: 500px; margin: auto; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>Contact Us</h2>
    <form onsubmit="return validateForm()">
        {% csrf_token %}
        {{ form.as_p }}
        <p id="error" class="error"></p>
        <button type="submit">Submit</button>
    </form>
</body>
</html>


6. JavaScript Form Validation

function validateForm() {
    const name = document.getElementById("id_name").value.trim();
    const email = document.getElementById("id_email").value.trim();
    const message = document.getElementById("id_message").value.trim();
    const error = document.getElementById("error");

    // Clear old error
    error.innerText = "";

    if (name === "" || email === "" || message === "") {
        error.innerText = "All fields are required.";
        return false;
    }

    // Simple email regex
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        error.innerText = "Enter a valid email.";
        return false;
    }

    if (message.length < 10) {
        error.innerText = "Message must be at least 10 characters.";
        return false;
    }

    return true;
}

7. Run the Server

python manage.py runserver


Practical Example:

3) Write a Django project where JavaScript is used to validate a patient
registration form on the client side.


Step 1: Create Project & App

django-admin startproject patient_project
cd patient_project
python manage.py startapp registration

Step 2: settings.py Configuration

INSTALLED_APPS = [
    ...
    'registration',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'registration' / 'static']


Step 3: Create Form

from django import forms

class PatientForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    symptoms = forms.CharField(widget=forms.Textarea)


Step 4: Create View

from django.shortcuts import render
from .forms import PatientForm

def register_patient(request):
    form = PatientForm()
    return render(request, 'registration/patient_form.html', {'form': form})

Step 5: URLs

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
]

registration/urls.py

from django.urls import path
from .views import register_patient

urlpatterns = [
    path('', register_patient, name='register_patient'),
]

Step 6: HTML Template

{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Patient Registration</title>
    <script src="{% static 'registration/script.js' %}"></script>
    <style>
        body { font-family: Arial; padding: 20px; }
        form { max-width: 600px; margin: auto; }
        input, textarea { width: 100%; margin: 10px 0; padding: 10px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>Patient Registration Form</h2>
    <form onsubmit="return validateForm()">
        {% csrf_token %}
        {{ form.as_p }}
        <p id="error" class="error"></p>
        <button type="submit">Register</button>
    </form>
</body>
</html>

Step 7: JavaScript Validation

function validateForm() {
    const name = document.getElementById("id_name").value.trim();
    const age = document.getElementById("id_age").value.trim();
    const email = document.getElementById("id_email").value.trim();
    const symptoms = document.getElementById("id_symptoms").value.trim();
    const error = document.getElementById("error");

    error.innerText = "";

    if (!name || !age || !email || !symptoms) {
        error.innerText = "All fields are required.";
        return false;
    }

    if (isNaN(age) || age <= 0) {
        error.innerText = "Please enter a valid age.";
        return false;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        error.innerText = "Invalid email format.";
        return false;
    }

    if (symptoms.length < 10) {
        error.innerText = "Symptoms description must be at least 10 characters.";
        return false;
    }

    return true;
}

-Then Run Your Server

python manage.py runserver



