15.Google Maps Geocoding API 
 
Theory: 
 
•Using Google Maps Geocoding API to convert addresses into coordinates. 

Ans:-

.What is Geocoding?
Geocoding is the process of converting a human-readable address (like "Taj Mahal, Agra,
India") into geographic coordinates (latitude and longitude), which can then be used to place
markers or calculate distances on maps.

What is the Google Maps Geocoding API?
                                                                 
The Google Maps Geocoding API is a web service provided by Google that allows you to:

Convert addresses → coordinates (geocoding)

Convert coordinates → addresses (reverse geocoding)

Get detailed location info (like postal codes, cities, regions)






Lab: 
 
•Create a Django project that takes an address as input and returns the latitude and longitude. 


Ans:-

1.Install Django and Requests

pip install django requests


2.Create Django Project and App

django-admin startproject geo_locator
cd geo_locator
python manage.py startapp location
                                                                
3.Add App to Installed Apps
In geo_locator/settings.py:


INSTALLED_APPS = [
    ...
    'location',
]

4.Create View to Handle Address Input

                                                                 # location/views.py

import requests
from django.http import JsonResponse

def get_coordinates(request):
    address = request.GET.get('address')
    if not address:
        return JsonResponse({'error': 'Address parameter is required'}, status=400)

    api_key = 'YOUR_GOOGLE_API_KEY'  # Replace with your actual API key
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return JsonResponse({
            'address': address,
            'latitude': location['lat'],
            'longitude': location['lng']
        })
    else:
        return JsonResponse({'error': 'Could not geocode the address'}, status=400)

5.Create URLs for the App

# location/urls.py

from django.urls import path
from .views import get_coordinates

urlpatterns = [
    path('get-coordinates/', get_coordinates),
]

In geo_locator/urls.py, include the app URLs:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', include('location.urls')),
]

6.Run the Server

python manage.py runserver
