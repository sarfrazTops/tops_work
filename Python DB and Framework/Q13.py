13.Django Forms and Authentication.

Theory: 
 
•Using Django’s built-in form handling.

Django provides a powerful built-in system to handle forms. This system is used to collect,
validate, and save data from HTML forms easily.

-What is Django Form Handling?

Ans:-

Django’s form handling means:

Showing a form on a web page

Taking user input

Validating the input

Saving the data to the database (if needed)

-Types of Forms in Django:

forms.Form – Used for manual fields (not linked to models)

forms.ModelForm – Used to create a form from a Django model (auto handles saving data)


•Implementing Django’s authentication system (sign up, login, logout, password management).

Ans:-

Django provides a built-in authentication system to manage:

User sign-up (registration)

User login and logout

Password change and reset

User sessions and permission


Main Features:
    
Secure password storage (hashed)

Built-in views and forms for login, logout, and password management

Middleware to manage sessions and users

Easy integration using django.contrib.auth


1. Sign Up (User Registration)

To allow users to register:

Create a custom registration form using UserCreationForm

Save the new user in the view


# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


Example:

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

2. Login (User Authentication)

Django has a built-in LoginView

You can also use your own view and authenticate() + login() functions

Example View:

from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


3. Logout

To log the user out:

from django.contrib.auth import logout

def logout_user(request):
    logout(request)


4. Password Management

Django provides built-in views for:

Change Password: PasswordChangeView

Reset Password by Email: PasswordResetView, PasswordResetConfirmView

from django.contrib.auth.forms import PasswordChangeForm


5. URLs for Authentication (Using Django built-ins)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]

Django’s authentication system helps developers manage users easily and securely with built-in tools for sign-up,
login, logout, and password management.


Lab: 
 
•Create a Django project for user registration and login functionality.

1. Create Project & App

django-admin startproject auth_project
cd auth_project
python manage.py startapp accounts

2. Update settings.py
In INSTALLED_APPS, add:

'accounts',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',


3. Create forms.py in accounts

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


4. Create Views (views.py in accounts)

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after registration
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

5. URLs Configuration

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

(b) Include in auth_project/urls.py:

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('accounts.urls')),
]

6. Templates

register.html

<h2>Register</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
<a href="{% url 'login' %}">Login</a>

login.html

<h2>Login</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Register</a>


Final Steps

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Practical Example:
    
13) Write a Django project to handle user sign up, login, password reset, and profile updates. 

Ans:-

1. Create Django Project & App

django-admin startproject user_auth_project
cd user_auth_project
python manage.py startapp accounts

2. Update settings.py
Add app and email settings:


INSTALLED_APPS = [
    'accounts',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

# Dummy email for password reset 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

3. Create Forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# SignUp Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

4. Create Views

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileUpdateForm

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Profile view
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Profile update
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form': form})


5. URLs Configuration

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),

    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password reset views
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

(b) user_auth_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]

Example: signup.html

<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>


Example: login.html

<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>


Example: profile.html

<h2>Welcome, {{ user.username }}</h2>
<a href="{% url 'profile_update' %}">Update Profile</a> |
<a href="{% url 'logout' %}">Logout</a>

7. Run the Project

python manage.py makemigrations
python manage.py migrate
python manage.py runserver



