11.RESTful API Design 

Theory: 

•REST principles: statelessness, resource-based URLs, and using HTTP methods for CRUD operations. 

. Statelessness

Every API request is independent.

The server does not store any session or user state between requests.

Each request must contain all necessary information (like authentication tokens).

Example:

GET /doctors/1
Authorization: Bearer <token>

2. Resource-Based URLs

REST APIs treat everything as a resource.

Resources (like users, doctors, etc.) are accessed using clean and meaningful URLs.

Example URLs:

GET    /doctors          → list all doctors
POST   /doctors          → create a new doctor
GET    /doctors/1        → get details of doctor with ID 1
PUT    /doctors/1        → update doctor with ID 1
DELETE /doctors/1        → delete doctor with ID 1


3. Using HTTP Methods for CRUD

HTTP Method	Operation	Description
GET	Read	Fetch data
POST	Create	Create new resource
PUT/PATCH	Update	Modify existing resource

Example:

POST /doctors
{
  "name": "sarfraz. Khan",
  "specialty": "Cardiologist"
}
DELETE	Delete	Remove a resource


Lab: 
 
•Design a REST API for managing doctor profiles using Django REST Framework.

1 Model: Doctor

# doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
2 Serializer: DoctorSerializer

# doctors/serializers.py

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

3 Views: Class-Based Views



from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

4 URLs

# doctors/urls.py

from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
]

Add to main urls.py:

# project_root/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctors.u

6 Install & Run

pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Practical Example:

11) Write a Django REST API with endpoints for creating, reading, updating, and deleting
    doctors.

Ans:-

1.Install Required Packages

pip install django djangorestframework

2.Start Project and App

django-admin startproject doctor_api
cd doctor_api
python manage.py startapp doctors

3.Update settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'doctors',
]


4.Create Doctor Model

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

6.Create Views

# doctors/views.py

from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

7.Add URLs


from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
]


And include this in your main project urls.py:


#doctor_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctors.urls')),
]

8.Apply Migrations and Run Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
