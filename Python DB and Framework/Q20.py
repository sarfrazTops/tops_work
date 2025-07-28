
20.Google Maps API 
 
Theory: 
 
•Integrating Google Maps API into Django projects. 

The Google Maps API allows you to embed and interact with maps in your Django web
applications. It is commonly used to display locations, search for nearby places, and
provide directions.


Get API Key:

Visit: https://console.developers.google.com

Enable Maps JavaScript API

Copy your API Key

2.Add Google Maps Script to Template:

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>

3.Create Map in HTML Template:


<div id="map" style="height: 400px; width: 100%;"></div>
<script>
    function initMap() {
        var location = {lat: 22.5726, lng: 88.3639};  // Example: Kolkata
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 10,
            center: location
        });
        var marker = new google.maps.Marker({position: location, map: map});
    }
</script>

 
Lab: 
 
•Use Google Maps API to display doctor locations in the "Doctor Finder" project.

Ans:-

Step 1: Get Google Maps API Key

Visit: https://console.developers.google.com

Enable: Maps JavaScript API

Copy your API Key

Step 2: Update Django Model (Optional – if not already)
In models.py of your doctor app:

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


Step 3: Create a View to Pass Doctor Data

from django.shortcuts import render
from .models import Doctor

def map_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'map.html', {'doctors': doctors})

Step 4: Create Template map.html

<!DOCTYPE html>
<html>
<head>
    <title>Doctor Locations</title>
    <style>
        #map {
            height: 500px;
            width: 100%;
        }
    </style>
</head>
<body>
    <h2>Doctor Locations on Map</h2>
    <div id="map"></div>

    <script>
        function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 5,
                center: {lat: 22.9734, lng: 78.6569}  // Center of India
            });

            var doctors = {{ doctors|safe }};
            {% for doc in doctors %}
                var marker = new google.maps.Marker({
                    position: {lat: {{ doc.latitude }}, lng: {{ doc.longitude }}},
                    map: map,
                    title: "{{ doc.name }}"
                });
            {% endfor %}
        }
    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
</body>
</html>


Step 5: Configure URL
In urls.py:


from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
]


Practical Example: 

20)Write a Django project to display doctor locations using Google Maps API.

Ans:-

Step 1: Create Django Project and App

django-admin startproject doctorfinder
cd doctorfinder
python manage.py startapp doctors

Step 2: Define the Doctor Model in doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


Step 3: Register the Model in admin.py

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)


Step 4: Configure App and Migrate
In settings.py:


INSTALLED_APPS = [
    ...
    'doctors',
]


Then run:

python manage.py makemigrations
python manage.py migrate

Step 5: Create View in doctors/views.py

from django.shortcuts import render
from .models import Doctor

def doctor_map(request):
    doctors = Doctor.objects.all()
    return render(request, 'map.html', {'doctors': doctors})

Step 6: Configure URL in doctors/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.doctor_map, name='doctor_map'),
]

-Include it in doctorfinder/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
]


Step 7: Create Template map.html

<!DOCTYPE html>
<html>
<head>
    <title>Doctor Map</title>
    <style>
        #map {
            height: 500px;
            width: 100%;
        }
    </style>
</head>
<body>
    <h2>Doctor Locations</h2>
    <div id="map"></div>

    <script>
        function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 5,
                center: {lat: 23.2599, lng: 77.4126}  // Center of India
            });

            {% for doctor in doctors %}
                var marker = new google.maps.Marker({
                    position: {lat: {{ doctor.latitude }}, lng: {{ doctor.longitude }}},
                    map: map,
                    title: "{{ doctor.name }} ({{ doctor.specialty }})"
                });
            {% endfor %}
        }
    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
</body>
</html>


Step 8: Insert Sample Doctor Data
Use Django Admin or shell:


python manage.py createsuperuser
python manage.py runserver
