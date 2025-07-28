Practical Example:

23) Write a Django project that integrates Google Maps API to show doctor locations in a
    specific city.

Ans:-

1. Start Django Project

django-admin startproject doctor_locator
cd doctor_locator
python manage.py startapp maps

2. Create the Doctor Model

# maps/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.city}


Run migrations:

python manage.py makemigrations
python manage.py migrate


3. Add Sample Data
Use admin panel or shell:

# Sample in shell
from maps.models import Doctor
Doctor.objects.create(name="Dr. Meera Patel", specialization="Cardiologist", city="Ahmedabad", latitude=23.0225, longitude=72.5714)
Doctor.objects.create(name="Dr. Rajiv Shah", specialization="Dentist", city="Ahmedabad", latitude=23.0300, longitude=72.5800)
Doctor.objects.create(name="Dr. Sneha Roy", specialization="Pediatrician", city="Surat", latitude=21.1702, longitude=72.8311)


4. Create View to Filter by City and Show Map

# maps/views.py

from django.shortcuts import render
from .models import Doctor

def map_view(request):
    city = request.GET.get('city', '')  # e.g., "Ahmedabad"
    doctors = Doctor.objects.filter(city__iexact=city) if city else []
    return render(request, 'maps/map.html', {
        'doctors': doctors,
        'city': city,
        'google_api_key': 'YOUR_GOOGLE_MAPS_API_KEY'
    })

5. URL Configuration

# maps/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),
]


nclude it in the main urls.py:


# doctor_locator/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maps.urls')),
]

6. HTML Template

<!-- templates/maps/map.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Doctors in {{ city }}</title>
    <script src="https://maps.googleapis.com/maps/api/js?key={{ google_api_key }}"></script>
</head>
<body>
    <h2>Doctor Locations in {{ city }}</h2>

    <form method="get">
        <input type="text" name="city" placeholder="Enter city name" value="{{ city }}">
        <button type="submit">Search</button>
    </form>

    {% if doctors %}
    <div id="map" style="height: 500px; width: 100%; margin-top: 20px;"></div>
    <script>
        function initMap() {
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: { lat: {{ doctors.0.latitude }}, lng: {{ doctors.0.longitude }} },
            });

            {% for doctor in doctors %}
            new google.maps.Marker({
                position: { lat: {{ doctor.latitude }}, lng: {{ doctor.longitude }} },
                map: map,
                title: "{{ doctor.name }} - {{ doctor.specialization }}",
            });
            {% endfor %}
        }

        window.onload = initMap;
    </script>
    {% else %}
        {% if city %}
        <p>No doctors found in {{ city }}.</p>
        {% endif %}
    {% endif %}
</body>
</html>


Test the App
Run the Django server:


python manage.py runserver
