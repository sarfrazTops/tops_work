10. Form Validation using JavaScript

Theory:
    
• Using JavaScript for front-end form validation.

Front-end form validation is the process of checking user input in a web form before
it is submitted to the server. It ensures that users enter correct and complete information.

Provides instant feedback to the user

Reduces unnecessary server load

Improves user experience

Prevents submission of incomplete or incorrect data

Practical Example:
    
10)Write a Django project that uses JavaScript to validate fields like
email and phone number in a registration form.

1. Project Setup
Create Project and App

django-admin startproject userproject
cd userproject
python manage.py startapp registration

Add App to Settings

INSTALLED_APPS = [
    ...
    'registration',
]

2. Create URLs
Project-level userproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
]

App-level registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
]

3. Create the View

from django.shortcuts import render

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        
        return render(request, 'registration/success.html', {'name': name})
    return render(request, 'registration/register.html')


4. Create Templates

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <script>
        function validateForm() {
            var email = document.getElementById("email").value;
            var phone = document.getElementById("phone").value;
            var emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
            var phonePattern = /^[0-9]{10}$/;

            if (!emailPattern.test(email)) {
                alert("Invalid email format");
                return false;
            }

            if (!phonePattern.test(phone)) {
                alert("Phone must be 10 digits");
                return false;
            }

            return true;
        }
    </script>
</head>
<body>
    <h2>User Registration</h2>
    <form method="post" onsubmit="return validateForm()">
        {% csrf_token %}
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="text" name="email" id="email" required><br><br>
        Phone: <input type="text" name="phone" id="phone" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>

success.html

<!DOCTYPE html>
<html>
<head><title>Success</title></head>
<body>
    <h2>Registration Successful!</h2>
    <p>Welcome, {{ name }}</p>
    <a href="/">Go back</a>
</body>
</html>


5. Run the Project

python manage.py runserver

