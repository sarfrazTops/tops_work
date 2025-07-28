6.URL Routing in Django REST Framework


Theory: 
 
•Defining URLs and linking them to views.

Ans:-
 
In Django and Django REST Framework (DRF), URLs act as the "address" for your API.
They connect user requests to specific views, which return data or perform actions.


1. Import the View in urls.py

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView


2. Define URL Patterns

urlpatterns = [
    path('api/doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('api/doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]

 Final urls.py Example:

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('api/doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('api/doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]


Lab: 
 
•Set up URL routing in a Django project to link to CRUD API endpoints for doctors.

1. Create the App (if not already created)

python manage.py startapp doctorapp

2. Create Views for CRUD in doctorapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer

# List and Create
class DoctorListCreateAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, and Delete
class DoctorDetailAPIView(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


3. Create URLs for Doctor API in doctorapp/urls.py

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]


4. Include App URLs in Main Project urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctorapp.urls')),  
]


Practical Example:

6) Write a Django project that routes URLs to the views handling doctor CRUD operations
(/doctors, /doctors/<id>). 
 
Ans:-

1. Model – models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

2. Serializer – serializers.py

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']

3. Views – views.py


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetailAPIView(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


4. URLs for Doctor App – doctorapp/urls.py

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]


5. Main Project URLs – project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctorapp.urls')),  
]
