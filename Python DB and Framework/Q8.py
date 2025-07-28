8. Django Admin Panel

Theory:
    
• Introduction to Django’s built-in admin panel.

1)What is the Django Admin Panel?

Django's admin panel is a web-based interface that allows you to:

View, add, edit, and delete data from your models

Manage your application's data without writing any HTML, forms, or queries


-Key Features:
    
Auto-generated interface for model management

User authentication (login/logout for superusers and staff)

Permission control (add, edit, delete access for specific users)

Search and filter functionality

Customizable forms and views


• Customizing the Django admin interface to manage database records.

Django's admin panel is a powerful interface to manage database records. However, the
default layout is basic. Customization allows developers to control how data is displayed,
searched, filtered, and edited in the admin panel to improve usability and efficiency.

Lab:
    
• Set up and customize the Django admin panel to manage a "Doctor Finder" project.

1)Define the Doctor model in models.py:

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()

2)Make migrations and apply them:

python manage.py makemigrations
python manage.py migrate

3)Create a superuser to access the admin panel:

python manage.py createsuperuser

4)Register the model in admin.py:

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)


Step 2: Customize the Admin Interface

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience')  
    search_fields = ('name', 'specialty')               
    list_filter = ('specialty',)                        
    ordering = ('-experience',)                         

admin.site.register(Doctor, DoctorAdmin)

Step 3: Customize Admin Site Branding

admin.site.site_header = "Doctor Finder Admin"
admin.site.site_title = "Doctor Finder"
admin.site.index_title = "Welcome to the Doctor Finder Dashboard"

-Benefits of Customization

Easy to search and filter doctors by specialty

Display only the most relevant info (name, experience)

Save time during data entry and updates

Makes the admin panel look professional and project-specific


Practical Example:

8) Write a Django project to create an admin panel and add custom fields for managing doctor
information

1 Create the Project and App

django-admin startproject hospital_project
cd hospital_project
python manage.py startapp doctorapp

2)Configure the App

INSTALLED_APPS = [
    ...
    'doctorapp',
]

3)Define the Doctor Model (Custom Fields)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    available = models.BooleanField(default=True)

4)Create and Apply Migrations

python manage.py makemigrations
python manage.py migrate

5) Register and Customize Admin Panel

from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience', 'available')
    search_fields = ('name', 'specialty')
    list_filter = ('specialty', 'available')
    ordering = ('-experience',)
    fields = ('name', 'specialty', 'experience', 'contact', 'email', 'available')
    readonly_fields = ('email',)  

admin.site.register(Doctor, DoctorAdmin)

6)Create Superuser

python manage.py createsuperuser

7)Run the Server

python manage.py runserver
