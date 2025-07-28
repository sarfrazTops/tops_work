 
14.OpenWeatherMap API Integration

Theory:

    
•Introduction to OpenWeatherMap API and how to retrieve weather data. 

Ans:-

What is OpenWeatherMap API?

OpenWeatherMap API is a popular web-based service that provides:

Real-time weather data

Forecasts (hourly, daily)

Historical weather info

For any city or location in the world

It allows developers to integrate weather data into their applications using simple HTTP requests.

Key Features:
    
Global coverage of cities and coordinates

JSON responses

Current, forecast, and historical data

Supports metric, imperial, and standard units


Step 1: Get an API Key

Sign up at https://openweathermap.org/

Go to your account → API Keys → Copy your key

Free plan with API key (limited requests)


Step 2: Make a Request
Example (Current Weather by City Name):

URL:
https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric

Step 3: Response Example (JSON)

{
  "weather": [
    {"main": "Clear", "description": "clear sky"}
  ],
  "main": {
    "temp": 27.0,
    "humidity": 40
  },
  "name": "London"
}


OpenWeatherMap API provides real-time and forecasted weather data.
Developers use an API key to access data using HTTP requests, typically in JSON format.
It's widely used in apps that show weather info by city or coordinates.


Lab: 
 
•Create a Django project that fetches weather data for a given location.


1.Install Django

pip install django requests

2.Create Project and App

django-admin startproject weather_project
cd weather_project
python manage.py startapp weather


3.Add App to settings.py

INSTALLED_APPS = [
    ...
    'weather',
]


4.Create View to Fetch Weather

# weather/views.py

import requests
from django.http import JsonResponse

def get_weather(request):
    city = request.GET.get('city', 'London')  # default city

    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'  # replace with your key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
        }
        return JsonResponse(weather_info)

    except Exception as e:
        return JsonResponse({'error': 'Could not fetch weather data'}, status=400)


5.Configure URLs



from django.urls import path
from .views import get_weather

urlpatterns = [
    path('weather/', get_weather, name='get-weather'),
]


Include in the main project urls.py:

# weather_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather.urls')),
]

Run the Server

python manage.py runserver


 
Practical Example:

14) Write a Django project to fetch current weather data for a location using the
    OpenWeatherMap API. 

1.Install Dependencies

pip install django requests

2.Create Django Project and App

django-admin startproject weather_app
cd weather_app
python manage.py startapp weather

3.Configure settings.py

INSTALLED_APPS = [
    ...
    'weather',
]


4.Add Weather View

# weather/views.py

import requests
from django.http import JsonResponse

def get_weather(request):
    city = request.GET.get('city', 'Mumbai')  # default city
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
        return JsonResponse(weather)
    else:
        return JsonResponse({"error": "City not found"}, status=404)


5.Set Up URLs

# weather/urls.py

from django.urls import path
from .views import get_weather

urlpatterns = [
    path('current/', get_weather, name='current_weather'),
]


Link it in the main urls.py:

# weather_app/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
]


6.Run Server and Test

python manage.py runserver
