21. Payment Integration (PayPal, Stripe)

Theory:
    
• Introduction to integrating payment gateways like PayPal and Stripe.

Ans:-

What is a Payment Gateway?


A payment gateway is a service that allows websites or applications to process payments
securely. It acts as a middleman between the customer, the merchant (business), and the
financial institutions (like banks).

Why Integrate a Payment Gateway?

To accept online payments via credit/debit cards, UPI, or digital wallets.

To provide a secure and encrypted environment for transactions.

To automate payment confirmation and order processing.

To support international payments (e.g., PayPal, Stripe).

1.PayPal

A widely used international payment gateway.

Users can pay with PayPal accounts or cards.

Supports recurring payments and subscriptions.

Offers REST APIs for integration.

2.Stripe

Developer-friendly and highly customizable.

Supports card payments, wallets, bank transfers.

Excellent documentation and API support.

Popular for SaaS and e-commerce platforms.



Lab:

    
• Add Stripe payment functionality to a Django project.

1. Install Stripe Library

pip install stripe

2. Update settings.py

# settings.py

STRIPE_PUBLIC_KEY = 'your_stripe_publishable_key'
STRIPE_SECRET_KEY = 'your_stripe_secret_key'


3. Set Up Views in views.py

# views.py

from django.conf import settings
from django.shortcuts import render, redirect
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'home.html')

def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': 1000,  # $10.00
                'product_data': {
                    'name': 'Sample Product',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return redirect(session.url)

4. Add URLs in urls.py

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('cancel/', lambda request: render(request, 'cancel.html'), name='cancel'),
]


5. Create Templates

<!DOCTYPE html>
<html>
<head>
    <title>Stripe Payment</title>
</head>
<body>
    <h2>Buy Sample Product - $10</h2>
    <form action="{% url 'create_checkout_session' %}" method="POST">
        {% csrf_token %}
        <button type="submit">Pay with Stripe</button>
    </form>
</body>
</html>


Practical Example:

21) Write a Django project to allow users to make payments via Stripe
for booking doctor appointments.

Ans:-

1. Project Setup

django-admin startproject doctor_payment
cd doctor_payment
python manage.py startapp appointments

Add 'appointments' to INSTALLED_APPS in settings.py.

Install Stripe:


pip install stripe


2. Stripe Configuration
In settings.py:


STRIPE_PUBLIC_KEY = 'your_publishable_key'
STRIPE_SECRET_KEY = 'your_secret_key'

3. Models (appointments/models.py)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    fee = models.IntegerField()  # in cents

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    email = models.EmailField()
    paid = models.BooleanField(default=False)


4. Views (appointments/views.py)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Appointment
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        patient_name = request.POST['name']
        email = request.POST['email']
        appointment = Appointment.objects.create(
            doctor=doctor,
            patient_name=patient_name,
            email=email
        )

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': doctor.fee,
                    'product_data': {
                        'name': f'Appointment with Dr. {doctor.name}',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

        appointment.paid = True
        appointment.save()
        return redirect(session.url, code=303)

    return render(request, 'appointments/book_appointment.html', {'doctor': doctor})

def success_view(request):
    return render(request, 'appointments/success.html')

def cancel_view(request):
    return render(request, 'appointments/cancel.html')


5. URLs (appointments/urls.py)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
]


Include in the main urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
]

 6. Templates
doctor_list.html

html
Copy
Edit
<h2>Available Doctors</h2>
<ul>
  {% for doctor in doctors %}
    <li>
      {{ doctor.name }} ({{ doctor.specialization }}) - ${{ doctor.fee|floatformat:2 }}
      <a href="{% url 'book_appointment' doctor.id %}">Book</a>
    </li>
  {% endfor %}
</ul>

book_appointment.html


<h2>Book Appointment with Dr. {{ doctor.name }}</h2>
<form method="post">
    {% csrf_token %}
    Name: <input type="text" name="name" required><br>
    Email: <input type="email" name="email" required><br>
    <button type="submit">Pay ${{ doctor.fee|floatformat:2 }}</button>
</form>

success.html


<h2>Payment Successful! Appointment Booked.</h2>
cancel.html


<h2>Payment Cancelled.</h2>
