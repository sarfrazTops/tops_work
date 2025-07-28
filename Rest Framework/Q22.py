22. Google Maps API Integration


Theory:
    
• Using Google Maps API to display maps and calculate distances between locations.

Ans:-

 What is the Google Maps API?
 
The Google Maps API is a set of web services provided by Google that allows developers to
integrate maps, geolocation, and route calculation into websites or apps.


Common Uses in Web Development:
Displaying Interactive Maps

Showing Locations (e.g., hospitals, doctors, stores)

Calculating Distance and Travel Time

Route Directions (Driving, Walking, Transit)

Geocoding and Reverse Geocoding (convert address ↔ coordinates)


Benefits of Using Google Maps API

Highly accurate and real-time data.

Customizable maps and routes.

Ideal for location-based services (e.g., doctor finder, delivery app).

Easy integration with JavaScript and Python/Django (via HTTP requests).



Lab:-

• Use Google Maps API to display doctor locations on a map.

1. Project Setup
Create a Django project and app:

django-admin startproject doctor_map
cd doctor_map
python manage.py startapp maps


2. Define Doctor Model
In maps/models.py:


from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

Run migrations:


python manage.py makemigrations
python manage.py migrate

3. Create Sample Doctors
You can use Django admin or shell:


# In Django shell
from maps.models import Doctor
Doctor.objects.create(name="Dr. A Sharma", specialization="Cardiologist", latitude=22.3039, longitude=70.8022)
Doctor.objects.create(name="Dr. B Mehta", specialization="Pediatrician", latitude=22.3072, longitude=73.1812

4. Create View to Display Doctors
In maps/views.py:

from django.shortcuts import render
from .models import Doctor

def map_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'maps/map.html', {'doctors': doctors, 'google_api_key': 'YOUR_GOOGLE_MAPS_API_KEY'})

5. URLs Setup
In maps/urls.py:


from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),
]
In the main urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maps.urls')),
]


Result:
When you run the server and visit the home page:

python manage.py runserver
