4.Requests and Responses in Django REST Framework



Theory: 
 
•HTTP request methods (GET, POST, PUT, DELETE).

ANS:-In web development and REST APIs, HTTP methods are used to perform actions like
    retrieving, creating, updating, or deleting data.

1. GET – Retrieve Data

Used to fetch data from the server.

Does not change any data.

2. POST – Create Data

Used to send data to the server to create a new resource.

3. PUT – Update Data

Used to completely update an existing resource.

4. DELETE – Remove Data

Used to delete a resource from the server.



•Sending and receiving responses in DRF.

ANS:-In Django REST Framework (DRF), we use views to handle HTTP requests and return
     responses using the Response class.


1. Receiving Requests

In DRF, when the client sends a request (like GET or POST), the view receives it using methods like:

def get(self, request): – For GET requests

def post(self, request): – For POST requests


2. Sending Responses
 
To send data back to the client, we use the Response class from rest_framework.response.


3. Using Serializers in Response
If you are working with models, use serializers to return structured data:


Lab: 
 

•Create a Django REST API that accepts POST requests to add new doctor profiles

ANS:-This API will accept POST requests with doctor details (like name, specialty, and
     contact), and save them into the database.


1. Model

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)


2. Serializer


from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']

3. API View to Handle POST Request


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorCreateAPIView(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


4. URL Configuration


from django.urls import path
from .views import DoctorCreateAPIView

urlpatterns = [
    path('api/doctors/add/', DoctorCreateAPIView.as_view(), name='doctor-add'),
]



Practical Example:

4) Write a Django project where the API accepts a POST request to add a doctor’s details to
   the database.


Step 1: Create Django Model

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
       return self.name
    
Step 2: Create Serializer

# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact']


Step 3: Create API View to Handle POST

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorSerializer

class AddDoctorAPIView(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


Step 4: Add URL Pattern

# urls.py
from django.urls import path
from .views import AddDoctorAPIView

urlpatterns = [
    path('api/add-doctor/', AddDoctorAPIView.as_view(), name='add-doctor'),
]


Example POST Request Body:

{
  "name": "Dr. Ramesh Gupta",
  "specialty": "Neurologist",
  "contact": "9876543210"
}


Example Response:

{
  "id": 1,
  "name": "Dr. Ramesh Gupta",
  "specialty": "Neurologist",
  "contact": "9876543210"
}

