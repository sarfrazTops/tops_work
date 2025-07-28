15.Customizing the Django Admin Panel

 
Theory: 
 
•Techniques for customizing the Django admin panel. 


Django’s admin panel is a built-in web interface that allows you to manage your database
models (add, update, delete, search) without writing custom views or form

You can customize the Django admin panel to make it more user-friendly, organized, and suitable
for your project needs.

1 Registering Models in admin.py

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)


2 Using ModelAdmin for Custom Display

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization')
    search_fields = ('name',)
    list_filter = ('specialization',)

admin.site.register(Doctor, DoctorAdmin)


3 Customizing Field Layout with fieldsets

class DoctorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'email')
        }),
        ('Details', {
            'fields': ('specialization',)
        }),
    )

4 Making Fields Read-Only

class DoctorAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)

5 Inline Models (ForeignKey Relationships)

class AppointmentInline(admin.TabularInline):
    model = Appointment

class DoctorAdmin(admin.ModelAdmin):
    inlines = [AppointmentInline]

6 Custom Admin Panel Title and Header

admin.site.site_header = "Hospital Admin"
admin.site.site_title = "Doctor Management System"
admin.site.index_title = "Welcome to Admin Dashboard"


7 Overriding Admin Templates (Advanced)

You can override Django admin templates like change_list.html, base_site.html for UI changes:

Create templates/admin/ folder and copy templates to customize

Example: Add logo or change footer

Lab: 
 
•Customize the Django admin panel for better management of records.

Ans:-


To customize the Django admin panel and improve record management:

Use list_display – Show important fields in the list view.


list_display = ('name', 'email', 'specialization')
Add search_fields – Enable search functionality.


search_fields = ('name', 'specialization')
Use list_filter – Add filters on the sidebar.


list_filter = ('specialization',)
Group fields using fieldsets – Organize form layout.


fieldsets = (('Basic Info', {'fields': ('name', 'email')}),)
Add inline models – Manage related models together using inlines.

Set custom admin titles – Improve branding.


admin.site.site_header = "Hospital Admin"
These features make the admin panel more organized, searchable, and user-friendly.


 
Practical Example: 15) Write a Django project that customizes the admin panel to display
more detailed doctor information (e.g., specialties, availability). 

1. Create a Django Project

django-admin startproject hospital
cd hospital
python manage.py startapp doctors

2. Define the Doctor Model (models.py)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    available_days = models.CharField(max_length=100)
    available_time = models.TimeField()

    def __str__(self):
        return self.name

3. Make Migrations

python manage.py makemigrations
python manage.py migrate

4. Customize the Admin Panel (admin.py)

from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization', 'available_days', 'available_time')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization', 'available_days')
    fieldsets = (
        ('Doctor Info', {
            'fields': ('name', 'email')
        }),
        ('Availability', {
            'fields': ('specialization', 'available_days', 'available_time')
        }),
    )

admin.site.register(Doctor, DoctorAdmin)


5. Create Superuser and Run the Server

python manage.py createsuperuser
python manage.py runserver

















