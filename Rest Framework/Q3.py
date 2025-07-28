3.Serialization in Django REST Framework


1.What is Serialization?

Ans:-

Serialization is the process of converting complex data (like Django models or Python objects) into a format that can be easily stored or shared, such as JSON or XML.

In Django REST Framework (DRF), serialization is used to:

Convert queryset or model data into JSON so it can be sent to the frontend or API users.

Also, convert incoming JSON data into Python objects to save to the database.


2.Converting Django QuerySets to JSON.

Ans:-

-A QuerySet is a collection of objects retrieved from the database using Django's ORM.

from django.core import serializers
from myapp.models import Doctor


doctors = Doctor.objects.all()


data = serializers.serialize('json', doctors)
print(data)


3.Using serializers in Django REST Framework (DRF). 

1. Create a Django Model


from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)


2. Create a Serializer

# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty']

# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

Practical Example:

3) Write a Django REST API to serialize a Doctor model with fields like name, specialty,
   and contact details.

ANS:-

1. Create the Model

# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
2. Create the Serializer

# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']

3. Create the API View

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

4. Set the URL

# urls.py
from django.urls import path
from .views import DoctorListAPIView

urlpatterns = [
    path('api/doctors/', DoctorListAPIView.as_view(), name='doctor-list'),
]


Output:-

[
  {
    "id": 1,
    "name": "Dr. Ayesha Khan",
    "specialty": "Cardiologist",
    "contact": "9876543210"
  },
  {
    "id": 2,
    "name": "Dr. Rahul Mehta",
    "specialty": "Dentist",
    "contact": "9123456789"
  }
]

 

