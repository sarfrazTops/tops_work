
13.Authentication and Authorization API 
 
Theory: 
 
•Difference between authentication and authorization.

Aspect	          Authentication	                           Authorization

Definition	   Verifies who the user is	  Determines what the user can access
Purpose	Confirms   identity (e.g., login)	  Grants permissions (e.g., access to resources)
Happens when?	   First (before authorization)	  After authentication
Example	User logs  in with email & password	  User is allowed to view their own doctor profile
Is it visible?	   Usually visible 	          Mostly hidden from users
Handled by	   username/password, tokens,     Roles, permissions, access control policies
                
Example:
    
Authentication: You log into a hospital system using your Google account.

Authorization: You can view your medical records but not edit other doctors’ profiles.

Authentication checks who you are, and authorization checks what you are allowed to do.
Both are essential for security in web applications.



Lab: 
 
•Implement user login, logout, and registration APIs in a Django project. 

1.Install Required Packages

pip install django djangorestframework djangorestframework-simplejwt

2.Start Django Project and App

django-admin startproject auth_api
cd auth_api
python manage.py startapp accounts

3.Update settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

4.Create Custom User Serializer

# accounts/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
5.Create Views for Registration

# accounts/views.py

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


6.Set Up JWT Login & Logout
In accounts/urls.py:

from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


In auth_api/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
]


7.Run Migrations and Start Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Practical Example:

13) Write a Django project that uses token-based authentication for users and restricts
    access to certain API endpoints.

Ans:-

1.Install Required Packages

pip install django djangorestframework

2.Create Project and App

django-admin startproject token_auth_api
cd token_auth_api
python manage.py startapp accounts

3.Configure settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

4.Create User Registration API

# accounts/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


5.Set Up Token Authentication

# accounts/urls.py

from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

Add to main urls.py:


# token_auth_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
]


6.Create a Protected API View

# accounts/views.py (add this view below RegisterView)

from rest_framework.views import APIView
from rest_framework.response import Response

class ProtectedView(APIView):
    def get(self, request):
        return Response({"message": "You are authenticated as " + request.user.username})


Add to urls.py:


from .views import ProtectedView

urlpatterns += [
    path('protected/', ProtectedView.as_view(), name='protected'),
]



7.Enable Token Creation Automatically
In accounts/apps.py:


from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals  # new

8.Run Migrations and Test

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
