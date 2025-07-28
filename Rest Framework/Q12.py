12.CRUD API (Create, Read, Update, Delete) 
 
Theory: 
 
•What is CRUD, and why is it fundamental to backend development?

Ans:-

What is CRUD?

CRUD stands for:

Letter	Operation	Description

 C	Create	        Add new data (e.g., a new user)
 R	Read	        View or retrieve data
 U	Update	        Modify existing data
 D	Delete	        Remove data


🔹 Why is CRUD Fundamental in Backend Development?

1.Core of Data Management:

Almost every backend application needs to store, retrieve, update, or delete data in a
database.

2.User Interaction:

CRUD operations allow users to:

Create accounts

View content

Edit profiles

Delete records, etc.

3.Foundation of APIs:

REST APIs are typically built around CRUD using HTTP methods:

POST → Create

GET → Read

PUT/PATCH → Update

DELETE → Delete

4.Database Integration:

Backend frameworks (like Django, Node.js, Laravel) use CRUD to interact with databases like MySQL, PostgreSQL, or MongoDB.

5.Scalable and Reusable:

Once CRUD is implemented, it becomes easy to extend functionality for more complex features.

CRUD represents the four basic operations of persistent storage — Create, Read, Update, and
Delete. It is the foundation of backend development because it allows systems to interact
with databases and manage data effectively.


 
Lab: 
 
•Implement a CRUD API using Django REST Framework for doctor profiles.

1.Install Requirements

pip install django djangorestframework


2.Create Django Project and App

django-admin startproject doctor_api
cd doctor_api
python manage.py startapp doctors

3.Configure settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'doctors',
]

4.Create the Doctor Model



from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

5.Create Serializer



from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


6.Create API Views



from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

7.Create URL Patterns

# doctors/urls.py

from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDeleteView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor-detail'),
]

Include this in your main urls.py:



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctors.urls')),
]

8.Migrate and Run

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Practical Example:

12) Write a Django project that allows users to create, read, update, and delete doctor
    profiles using API endpoints.

Ans:-

1.Install Required Packages

pip install django djangorestframework

2.Create Django Project and App

django-admin startproject doctor_crud
cd doctor_crud
python manage.py startapp doctors

3.Update settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'doctors',
]

4.Create the Doctor Model

# doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

5.Create Serializer

# doctors/serializers.py

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

6.Create API Views

# doctors/views.py

from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

7.Define URL Routes

# doctors/urls.py

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail'),
]

Include in the main project’s URL:

# doctor_crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctors.urls')),
]

8.Run Migrations and Start Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

