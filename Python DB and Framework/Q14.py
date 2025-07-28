14.CRUD Operations using AJAX 
 
Theory: 
 
•Using AJAX for making asynchronous requests to the server without reloading the page.

AJAX (Asynchronous JavaScript and XML) is a technology used to send and receive data from
the server without reloading the entire web page.

In Django, AJAX is commonly used with JavaScript or jQuery to make asynchronous requests
to views.

Example: Submit Form Using AJAX in Django

from django.http import JsonResponse
from .models import Contact

def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        Contact.objects.create(name=name, message=message)
        return JsonResponse({'status': 'Saved'})

2. URL (in urls.py)

from django.urls import path
from . import views

urlpatterns = [
    path('save-contact/', views.save_contact, name='save_contact'),
]

3. HTML + AJAX (in template)

<form id="contactForm">
    <input type="text" name="name" placeholder="Name">
    <textarea name="message" placeholder="Message"></textarea>
    <button type="submit">Submit</button>
</form>

<div id="result"></div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $('#contactForm').on('submit', function(e){
        e.preventDefault();
        $.ajax({
            url: '/save-contact/',
            type: 'POST',
            data: $(this).serialize(),
            headers: { 'X-CSRFToken': '{{ csrf_token }}' },
            success: function(response){
                $('#result').text(response.status);
            }
        });
    });
</script>



 
Lab: 
 
•Implement AJAX in a Django project for performing CRUD operations.

1. Project Setup

django-admin startproject ajax_crud_project
cd ajax_crud_project
python manage.py startapp students

2. Add to settings.py

INSTALLED_APPS = [
    'students',
    ...
]

3. Create the Model – students/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate

4. Forms – students/forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']

5. Views – students/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'students/student_list.html', {'students': students, 'form': form})

def save_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'course': student.course
            }
            return JsonResponse({'status': 'saved', 'student': data})
    return JsonResponse({'status': 'error'})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return JsonResponse({'status': 'deleted'})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            data = {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'course': student.course
            }
            return JsonResponse({'status': 'updated', 'student': data})
    return JsonResponse({'status': 'error'})

6. URLs – students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('save/', views.save_student, name='save_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
]

In ajax_crud_project/urls.py:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]


7. Template – students/templates/students/student_list.html

<h2>Student List</h2>

<form id="studentForm">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="text" name="course" placeholder="Course" required>
    <button type="submit">Add Student</button>
</form>

<ul id="studentList">
    {% for student in students %}
        <li id="student-{{ student.id }}">
            {{ student.name }} | {{ student.email }} | {{ student.course }}
            <button onclick="deleteStudent({{ student.id }})">Delete</button>
        </li>
    {% endfor %}
</ul>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $('#studentForm').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: "{% url 'save_student' %}",
            type: "POST",
            data: $(this).serialize(),
            success: function(response){
                if(response.status == 'saved'){
                    const s = response.student;
                    $('#studentList').append(
                        `<li id="student-${s.id}">${s.name} | ${s.email} | ${s.course}
                        <button onclick="deleteStudent(${s.id})">Delete</button></li>`
                    );
                    $('#studentForm')[0].reset();
                }
            }
        });
    });

    function deleteStudent(id){
        $.ajax({
            url: `/delete/${id}/`,
            type: 'GET',
            success: function(response){
                if(response.status == 'deleted'){
                    $('#student-' + id).remove();
                }
            }
        });
    }
</script>

-Final Steps

python manage.py runserver

AJAX is used in this Django project to handle CRUD operations without refreshing the page.
jQuery is used to send asynchronous POST and GET requests. Django processes these requests
using views and returns a JsonResponse. The page is updated dynamically using JavaScript
 
Practical Example:

14) Write a Django project that uses AJAX to add, edit, or delete doctor profiles without
   refreshing the page


1. Create Project & App

django-admin startproject doctor_ajax_project
cd doctor_ajax_project
python manage.py startapp doctors

 2. settings.py
Add the app:

INSTALLED_APPS = [
    ...,
    'doctors',
]

3. Create Model (doctors/models.py)

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate


4. Create Form

from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'specialization']

5. Views (doctors/views.py)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    form = DoctorForm()
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'form': form, 'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return JsonResponse({
                'status': 'success',
                'id': doctor.id,
                'name': doctor.name,
                'email': doctor.email,
                'specialization': doctor.specialization
            })
    return JsonResponse({'status': 'error'})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return JsonResponse({'status': 'deleted'})

def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            updated_doctor = form.save()
            return JsonResponse({
                'status': 'updated',
                'id': updated_doctor.id,
                'name': updated_doctor.name,
                'email': updated_doctor.email,
                'specialization': updated_doctor.specialization
            })
    return JsonResponse({'status': 'error'})

6. URLs


from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('update/<int:pk>/', views.update_doctor, name='update_doctor'),
]

In doctor_ajax_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
]

7. Template – doctors/templates/doctors/doctor_list.html

<!DOCTYPE html>
<html>
<head>
    <title>Doctor AJAX CRUD</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<h2>Add Doctor</h2>
<form id="doctorForm">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="text" name="specialization" placeholder="Specialization" required>
    <button type="submit">Add</button>
</form>

<hr>

<h2>Doctor List</h2>
<ul id="doctorList">
    {% for doc in doctors %}
    <li id="doctor-{{ doc.id }}">
        <span class="name">{{ doc.name }}</span> |
        <span class="email">{{ doc.email }}</span> |
        <span class="specialization">{{ doc.specialization }}</span>
        <button onclick="editDoctor({{ doc.id }})">Edit</button>
        <button onclick="deleteDoctor({{ doc.id }})">Delete</button>
    </li>
    {% endfor %}
</ul>

<script>
    // Add Doctor
    $('#doctorForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '{% url "add_doctor" %}',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                if (response.status == 'success') {
                    $('#doctorList').append(
                        `<li id="doctor-${response.id}">
                            <span class="name">${response.name}</span> |
                            <span class="email">${response.email}</span> |
                            <span class="specialization">${response.specialization}</span>
                            <button onclick="editDoctor(${response.id})">Edit</button>
                            <button onclick="deleteDoctor(${response.id})">Delete</button>
                        </li>`
                    );
                    $('#doctorForm')[0].reset();
                }
            }
        });
    });

    // Delete Doctor
    function deleteDoctor(id) {
        $.ajax({
            url: `/delete/${id}/`,
            success: function(response) {
                if (response.status == 'deleted') {
                    $(`#doctor-${id}`).remove();
                }
            }
        });
    }

    // Edit Doctor (Simple Prompt Version)
    function editDoctor(id) {
        const name = prompt("Enter new name:");
        const email = prompt("Enter new email:");
        const specialization = prompt("Enter new specialization:");

        $.ajax({
            url: `/update/${id}/`,
            type: 'POST',
            data: {
                'name': name,
                'email': email,
                'specialization': specialization,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.status == 'updated') {
                    const doc = $(`#doctor-${id}`);
                    doc.find('.name').text(response.name);
                    doc.find('.email').text(response.email);
                    doc.find('.specialization').text(response.specialization);
                }
            }
        });
    }
</script>

</body>
</html>


Final Step

python manage.py runserver


In this project, we used AJAX and jQuery to perform CRUD operations on a Doctor model in
Django. Each request is handled asynchronously, and updates are shown without reloading the
page. This improves user experience and creates a fast, modern web interface.



 
Practical Example:

14) Write a Django project that uses AJAX to add, edit, or delete doctor profiles without
        refreshing the page. 

1. Create Project & App

django-admin startproject ajax_doctor
cd ajax_doctor
python manage.py startapp doctors

2. Update settings.py

INSTALLED_APPS = [
    ...
    'doctors',
]

3. Create Model – doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)


Run

python manage.py makemigrations
python manage.py migrate

4. Create Form – doctors/forms.py

from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'specialization']

5. Create Views – doctors/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor
from .forms import DoctorForm

def doctor_home(request):
    doctors = Doctor.objects.all()
    form = DoctorForm()
    return render(request, 'doctors/doctor_home.html', {'form': form, 'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return JsonResponse({
                'status': 'success',
                'id': doctor.id,
                'name': doctor.name,
                'email': doctor.email,
                'specialization': doctor.specialization
            })
    return JsonResponse({'status': 'error'})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return JsonResponse({'status': 'deleted'})

def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST, instance=doctor)
    if form.is_valid():
        updated = form.save()
        return JsonResponse({
            'status': 'updated',
            'id': updated.id,
            'name': updated.name,
            'email': updated.email,
            'specialization': updated.specialization
        })
    return JsonResponse({'status': 'error'})


6. URLs

(a) doctors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_home, name='doctor_home'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('update/<int:pk>/', views.update_doctor, name='update_doctor'),
]


(b) In ajax_doctor/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
]

7. Template –

<!DOCTYPE html>
<html>
<head>
    <title>AJAX Doctor Profiles</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<h2>Add Doctor</h2>
<form id="addDoctorForm">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="text" name="specialization" placeholder="Specialization" required>
    <button type="submit">Add</button>
</form>

<hr>

<h2>Doctor List</h2>
<ul id="doctorList">
    {% for doctor in doctors %}
    <li id="doctor-{{ doctor.id }}">
        <strong>{{ doctor.name }}</strong> - {{ doctor.email }} - {{ doctor.specialization }}
        <button onclick="editDoctor({{ doctor.id }})">Edit</button>
        <button onclick="deleteDoctor({{ doctor.id }})">Delete</button>
    </li>
    {% endfor %}
</ul>

<script>
    // Add Doctor
    $('#addDoctorForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: "{% url 'add_doctor' %}",
            type: "POST",
            data: $(this).serialize(),
            success: function(res) {
                if(res.status == 'success') {
                    $('#doctorList').append(
                        `<li id="doctor-${res.id}">
                            <strong>${res.name}</strong> - ${res.email} - ${res.specialization}
                            <button onclick="editDoctor(${res.id})">Edit</button>
                            <button onclick="deleteDoctor(${res.id})">Delete</button>
                        </li>`
                    );
                    $('#addDoctorForm')[0].reset();
                }
            }
        });
    });

    // Delete Doctor
    function deleteDoctor(id) {
        $.get(`/delete/${id}/`, function(res){
            if(res.status === 'deleted') {
                $(`#doctor-${id}`).remove();
            }
        });
    }

    // Edit Doctor (Simple prompt-based)
    function editDoctor(id) {
        const name = prompt("Enter new name:");
        const email = prompt("Enter new email:");
        const specialization = prompt("Enter new specialization:");
        $.post(`/update/${id}/`, {
            'name': name,
            'email': email,
            'specialization': specialization,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        }, function(res) {
            if(res.status == 'updated') {
                $(`#doctor-${id}`).html(
                    `<strong>${res.name}</strong> - ${res.email} - ${res.specialization}
                    <button onclick="editDoctor(${res.id})">Edit</button>
                    <button onclick="deleteDoctor(${res.id})">Delete</button>`
                );
            }
        });
    }
</script>

</body>
</html>

Final Step

python manage.py runserver
