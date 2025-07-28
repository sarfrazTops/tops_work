9.Project Setup 
 
Theory: 
 
•Setting up a Django REST Framework project.

Ans:-
 
Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs
in Django. It allows developers to create RESTful APIs easily using Django models and views.

1. Install Django and DRF

pip install django djangorestframework

2. Create a Django Project and App

django-admin startproject myproject
cd myproject
python manage.py startapp myapi


3. Add to INSTALLED_APPS

INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapi',
]


4. Create Models (Example: Doctor)
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

5. Create Serializer

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

6. Create Views

from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

7. Setup URLs

from rest_framework import routers
from .views import DoctorViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

In myproject/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
]

Practical Example:

9) Write a Django project to set up a new app called doctor_finder and create models,
   serializers, and views.

Ans:-

Step 1: Create a new Django project and app

django-admin startproject myproject
cd myproject
python manage.py startapp doctor_finder


Step 2: Register the app

INSTALLED_APPS = [
    ...
    'rest_framework',
    'doctor_finder',
]

Step 3: Create a model in doctor_finder/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

Step 4: Create a serializer in doctor_finder/serializers.py

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

Step 5: Create views in doctor_finder/views.py

from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

Step 6: Set up URLs

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

Include in myproject/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctor_finder.urls')),
]

Step 7: Run Migrations

python manage.py makemigrations
python manage.py migrate


Step 8: Run the Server

python manage.py runserver


