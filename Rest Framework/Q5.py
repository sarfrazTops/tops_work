 
5.Views in Django REST Framework 


Theory:
    
•Understanding views in DRF: Function-based views vs Class-based views. 
 
1. Function-Based Views (FBV)

Views are written as simple Python functions.

Handle HTTP methods inside the function using decorators like @api_view.

Easy to write and understand for simple APIs.

Example:

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def doctor_list(request):
    doctors = ["Dr. A", "Dr. B"]
    return Response(doctors)


2. Class-Based Views (CBV)

Views are written as Python classes inheriting from DRF base classes like APIView.

HTTP methods (get, post, etc.) are defined as methods inside the class.

More flexible and reusable for complex APIs.

from rest_framework.views import APIView
from rest_framework.response import Response

class DoctorList(APIView):
    def get(self, request):
        doctors = ["Dr. A", "Dr. B"]
        return Response(doctors)

Lab: 
 
•Implement a class-based view in DRF for managing doctor profiles.

1. Model

# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

2. Serializer

# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']

3. Class-Based View

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorAPIView(APIView):

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


4. URL Configuration

# urls.py
from django.urls import path
from .views import DoctorAPIView

urlpatterns = [
    path('api/doctors/', DoctorAPIView.as_view(), name='doctor-api'),
]



Practical Example:

5) Write a Django project that implements a class-based view to handle doctor profile
   creation, reading, updating, and deletion (CRUD operations).


Ans:-


1. Model

# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


2. Serializer

# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']


3. Class-Based View for CRUD

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorDetailAPIView(APIView):

    # Get doctor by ID
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    # Update doctor by ID
    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete doctor by ID
    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorListCreateAPIView(APIView):

    # List all doctors
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    # Create a new doctor
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


4. URLs

# urls.py
from django.urls import path
from .views import DoctorListCreateAPIView, DoctorDetailAPIView

urlpatterns = [
    path('api/doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('api/doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
]

