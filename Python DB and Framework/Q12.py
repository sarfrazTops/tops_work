12. ORM and QuerySets

Theory:
    
• Understanding Django’s ORM and how QuerySets are used to interact with the database.

Ans:-

Django ORM (Object-Relational Mapping) is a built-in feature in Django that allows developers
to interact with the database using Python code instead of writing raw SQL queries.

It automatically maps Python classes (models) to database tables, making it easier and faster
to perform database operations like Create, Read, Update, and Delete (CRUD).

Benefits of Django ORM

Easy to use for beginners.

Avoids SQL injection.

Works with multiple database engines (SQLite, MySQL, PostgreSQL, etc.).

Allows you to write database queries using clean, readable Python code.



:-QuerySet

A QuerySet is a collection of database records retrieved from a Django model.

It represents rows in the database.

QuerySets are lazy, meaning they are only evaluated when needed.

You can use filtering, ordering, slicing, etc., on QuerySet


Example Model:

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

1.Using QuerySets (with Examples)

Student.objects.all()

2. Filter Records

Student.objects.filter(age=18)

3. Get a Single Record

Student.objects.get(id=1)

4. Create a New Record

Student.objects.create(name="Ali", age=20, email="ali@example.com")

5. Update a Record

student = Student.objects.get(id=1)
student.name = "Aman"
student.save()


6. Delete a Record

student = Student.objects.get(id=1)
student.delete()


Practical Example:

12) Write a Django project that demonstrates CRUD operations (Create, Read, Update, Delete)
on doctor profiles using Django ORM. 
 
Ans:-

1. Create Django Project & Ap

django-admin startproject doctor_crud
cd doctor_crud
python manage.py startapp doctors

2. settings.py (doctor_crud/settings.py)

INSTALLED_APPS = [
    ...
    'doctors',
]


3. Create Doctor Model (models.py in doctors app)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

4. Run Migrations

python manage.py makemigrations
python manage.py migrate


5. Create Forms (forms.py)

from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


6. Views for CRUD (views.py)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

# READ - List all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

# CREATE - Add a new doctor
def doctor_create(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_form.html', {'form': form})

# UPDATE - Edit doctor details
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_form.html', {'form': form})

# DELETE - Delete a doctor
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})


7. URLs Configuration

(a) In doctors/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_create, name='doctor_create'),
    path('edit/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),
]

(b) In doctor_crud/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
]


8. Templates

<h2>Doctor List</h2>
<a href="{% url 'doctor_create' %}">Add Doctor</a>
<table border="1">
  <tr><th>Name</th><th>Email</th><th>Specialization</th><th>Phone</th><th>Actions</th></tr>
  {% for doctor in doctors %}
  <tr>
    <td>{{ doctor.name }}</td>
    <td>{{ doctor.email }}</td>
    <td>{{ doctor.specialization }}</td>
    <td>{{ doctor.phone }}</td>
    <td>
      <a href="{% url 'doctor_update' doctor.pk %}">Edit</a> |
      <a href="{% url 'doctor_delete' doctor.pk %}">Delete</a>
    </td>
  </tr>
  {% endfor %}
</table>


(c) doctor_form.html

<h2>Doctor Form</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>


(d) doctor_confirm_delete.html

<h2>Are you sure you want to delete "{{ doctor.name }}"?</h2>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, Delete</button>
    <a href="{% url 'doctor_list' %}">Cancel</a>
</form>



(e)Run the Project

python manage.py runserver

















