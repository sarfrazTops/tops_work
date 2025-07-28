16.Payment Integration Using Paytm

Theory: 

Payment gateways allow secure online transactions. In Django, integrating a payment gateway like Paytm involves:

Merchant Setup: Register on Paytm to get Merchant ID, Merchant Key, etc.

Install SDK/API: Use Paytm’s official Python SDK or REST API for integration.

Payment Request: Create a payment form in Django and send the request to Paytm.

Redirect to Paytm: The user is redirected to Paytm's secure payment page.

Callback Handling: After payment, Paytm sends a response to a Django view (callback URL).

Transaction Verification: Use Paytm’s checksum and status APIs to verify payment.

This allows users to make safe payments and the system to confirm and record them.


 
Lab: 
 
1•Implement Paytm payment gateway in a Django project.

Create a Django Project and App

django-admin startproject paytmdemo
cd paytmdemo
python manage.py startapp payments

2.Install Required Package

pip install django

3.Create Payment Form

<form method="post" action="{% url 'pay' %}">
    {% csrf_token %}
    <input type="text" name="amount" placeholder="Enter Amount" required />
    <button type="submit">Pay with Paytm</button>
</form>

4.views.py (payments/views.py)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json

MERCHANT_ID = 'Your-Merchant-ID'
MERCHANT_KEY = 'Your-Merchant-Key'

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def pay(request):
    if request.method == 'POST':
        amount = request.POST['amount']
               return HttpResponse("Redirect to Paytm with payment details")


5.URL Configuration (urls.py)

from django.contrib import admin
from django.urls import path
from payments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pay/', views.pay, name='pay'),
]


Practical Example:

16) Write a Django project that integrates Paytm for handling payments in the "Doctor Finder"
project. 

1. Create Django Project and App

django-admin startproject doctorfinder
cd doctorfinder
python manage.py startapp appointments

2. Add App to settings.py

INSTALLED_APPS = [
    ...
    'appointments',
]

3. Create HTML Form (book_appointment.html)

<form method="POST" action="{% url 'initiate_payment' %}">
  {% csrf_token %}
  <input type="text" name="doctor_name" placeholder="Doctor Name" required />
  <input type="number" name="amount" placeholder="Fees (₹)" required />
  <button type="submit">Pay Now with Paytm</button>
</form>


4. Views (appointments/views.py)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import uuid

def book_appointment(request):
    return render(request, 'book_appointment.html')

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        doctor_name = request.POST['doctor_name']
        amount = request.POST['amount']
        order_id = str(uuid.uuid4())
                return HttpResponse(f"Redirecting to Paytm payment gateway for Rs. {amount}")

5. URLs (appointments/urls.py)

from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book'),
    path('pay/', views.initiate_payment, name='initiate_payment'),
]


:-In main doctorfinder/urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
]
