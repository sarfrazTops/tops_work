18.REST Countries API Integration 
 
Theory: 
 
•Introduction to REST Countries API and how to retrieve country-specific data. 

Ans:-

What is the REST Countries API?

The REST Countries API is a public web API that provides country-related data in JSON format. It's widely used for educational, geographic, or travel-related applications.

Developers can access detailed information about countries, including:

Name, capital, population

Languages, currencies, and region

Flags, borders, timezones, and more

API Base URL

https://restcountries.com/
The most common version in use is v3.1, so the base path becomes:


https://restcountries.com/v3.1/

 
Lab: 
 
•Use REST Countries API to fetch data for a specific country. 

Ans:-

Use the REST Countries API to:

Take a country name as input

Fetch and display key information like:

Capital

Region

Population

Currency

Languages

Flag


API Used
Endpoint:

GET https://restcountries.com/v3.1/name/{country}

Python Example Using requests
Install the library (if needed)

pip install requests


Code:

import requests

def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # First match
        name = data['name']['common']
        capital = data.get('capital', ['N/A'])[0]
        region = data['region']
        population = data['population']
        currencies = list(data['currencies'].keys())
        languages = list(data['languages'].values())
        flag_url = data['flags']['png']

        print(f" Country: {name}")
        print(f" Capital: {capital}")
        print(f" Region: {region}")
        print(f"Population: {population}")
        print(f"Currency: {', '.join(currencies)}")
        print(f"Languages: {', '.join(languages)}")
        print(f" Flag URL: {flag_url}")
    else:
        print(" Country not found or API error.")

# Example usage
get_country_data("India")


Sample Output:-

Country: India
Capital: New Delhi
Region: Asia
Population: 1380004385
Currency: INR
Languages: Hindi, English
Flag URL: https://flagcdn.com/w320/in.png


Practical Example:

18) Write a Django project that displays details (population, language, currency) of a
    country entered by the user using the REST Countries API.

Ans:-

1.Create Project and App

django-admin startproject country_info_project
cd country_info_project
python manage.py startapp country_app

2.Install requests

pip install requests

3.Add country_app to INSTALLED_APPS in settings.py

INSTALLED_APPS = [
    ...
    'country_app',
]


4.forms.py (in country_app/)

from django import forms

class CountryForm(forms.Form):
    name = forms.CharField(label='Enter Country Name', max_length=100)


5.views.py

from django.shortcuts import render
import requests
from .forms import CountryForm

def get_country_details(request):
    data = {}
    error = None

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country_name = form.cleaned_data['name']
            url = f"https://restcountries.com/v3.1/name/{country_name}"
            response = requests.get(url)

            if response.status_code == 200:
                try:
                    country = response.json()[0]
                    data['population'] = country['population']
                    data['languages'] = ', '.join(country['languages'].values())
                    data['currency'] = ', '.join([curr for curr in country['currencies'].keys()])
                except Exception as e:
                    error = "Data format error."
            else:
                error = "Country not found or API error."
    else:
        form = CountryForm()

    return render(request, 'country_app/country_form.html', {'form': form, 'data': data, 'error': error})


6.urls.py (in country_app/)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_country_details, name='get_country_details'),
]

7.urls.py (in country_info_project/)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('country_app.urls')),
]

8.Template: country_form.html

<!DOCTYPE html>
<html>
<head>
    <title>Country Info</title>
</head>
<body>
    <h2>Get Country Details</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Fetch Info</button>
    </form>

    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    {% if data %}
        <h3>Results:</h3>
        <p><strong>Population:</strong> {{ data.population }}</p>
        <p><strong>Languages:</strong> {{ data.languages }}</p>
        <p><strong>Currency:</strong> {{ data.currency }}</p>
    {% endif %}
</body>
</html>


Run the Server

python manage.py runserver
