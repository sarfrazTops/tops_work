7.Pagination in Django REST Framework 

Theory: 
 
•Adding pagination to APIs to handle large data sets.

When dealing with large datasets in APIs, it's not efficient or practical to return all
records at once. Pagination is a technique used to split data into smaller chunks (pages)
so that only a portion of the data is sent at a time. This improves performance, reduces
server load, and provides a better user experience.


.Common Pagination Methods:

1.Limit and Offset

-GET /doctors?limit=10&offset=20

-Returns 10 records starting from the 21st record


2.Page and Size

-GET /doctors?page=3&size=10

-Returns page 3 with 10 results per page.


3.Cursor-based Pagination

Uses a pointer (like a unique ID or timestamp) to retrieve the next set.

Example: GET /doctors?cursor=abc123


Types of Paginators in DRF:
    
PageNumberPagination

LimitOffsetPagination

CursorPagination

 
Lab: 
 
•Implement pagination in a Django REST API for fetching doctor profiles. 


1. Create a Django Project and App

django-admin startproject doctor_api
cd doctor_api
python manage.py startapp doctors


2. Define the Doctor Model (doctors/models.py)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

3. Create and Apply Migrations

python manage.py makemigrations
python manage.py migrate

4. Register Model in Admin Panel (optional)

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)

5. Create a Serializer (doctors/serializers.py)

from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


6. Create a View with Pagination (doctors/views.py)

from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


7. Add Pagination in settings.py


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

8. Set Up URLs

Project URL (doctor_api/urls.py)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('doctors.urls')),
]


App URL (doctors/urls.py)

from django.urls import path
from .views import DoctorListView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
]

Practical Example:

7) Write a Django API that returns paginated results for a list of doctors. 

