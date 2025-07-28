16.GitHub API Integration 
 
Theory: 
 
•Introduction to GitHub API and how to interact with repositories, pull requests, and issues. 

Ans:-

What is the GitHub API?

The GitHub API allows developers to interact programmatically with GitHub, a platform used for hosting and managing code repositories. Using this API, users can perform actions like:

-Creating or updating repositories

-Managing pull requests

-Handling issues

-Accessing commit histories

-Managing user data and collaborators


How to Use GitHub API
GitHub REST API endpoints usually follow this pattern:

https://api.github.com/...



Lab: 
 
•Use GitHub API to create a repository and retrieve user data.

Ans:-

Step 1: Generate a GitHub Personal Access Token (PAT)

Go to: https://github.com/settings/tokens

Click "Generate new token (classic)"

Select scopes like repo, user, etc.

Copy the token (you will need it in code)


Step 2: Python Script to Use GitHub API
Install Required Library:
    
pip install requests

-Python Code to Create a Repo and Fetch User Data

import requests


GITHUB_TOKEN = 'your_personal_access_token_here'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 1: Get Authenticated User Data
user_response = requests.get('https://api.github.com/user', headers=HEADERS)

if user_response.status_code == 200:
    user_data = user_response.json()
    print(" User Data Retrieved:")
    print("Username:", user_data['login'])
    print("Name:", user_data.get('name'))
    print("Public Repos:", user_data['public_repos'])
else:
    print(" Failed to get user data:", user_response.json())

# Step 2: Create a New Repository
repo_data = {
    "name": "my-demo-repo",
    "description": "This is a test repo created via GitHub API",
    "private": False
}

repo_response = requests.post('https://api.github.com/user/repos', headers=HEADERS, json=repo_data)

if repo_response.status_code == 201:
    print(" Repository created successfully!")
    print("Repo URL:", repo_response.json()['html_url'])
else:
    print(" Failed to create repository:", repo_response.json())


Output Example:

User Data Retrieved:
Username: sarfrazkhan
Name: Sarfraz Khan
Public Repos: 12

Repository created successfully!
Repo URL: https://github.com/sarfrazkhan/my-demo-repo


Practical Example:

16) Write a Django project that interacts with the GitHub API to create a new repository
    and list all repositories for a given user. 
 
Ans:-

1.Create a Django project and app

django-admin startproject github_api_project
cd github_api_project
python manage.py startapp github_app


2.Install requests for API calls

pip install requests

3.settings.py
Add 'github_app' to INSTALLED_APPS


4.forms.py (in github_app/)

from django import forms

class RepoForm(forms.Form):
    name = forms.CharField(label='Repository Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)

class UsernameForm(forms.Form):
    username = forms.CharField(label='GitHub Username')


5.views.py

from django.shortcuts import render
import requests
from .forms import RepoForm, UsernameForm

# Replace with your GitHub Personal Access Token
GITHUB_TOKEN = 'your_personal_access_token_here'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repo(request):
    message = ''
    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            data = {
                "name": form.cleaned_data['name'],
                "description": form.cleaned_data['description'],
                "private": False
            }
            response = requests.post('https://api.github.com/user/repos', headers=HEADERS, json=data)
            if response.status_code == 201:
                message = ' Repository created successfully!'
            else:
                message = f" Failed: {response.json().get('message')}"
    else:
        form = RepoForm()
    return render(request, 'github_app/create_repo.html', {'form': form, 'message': message})

def list_repos(request):
    repos = []
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            response = requests.get(f'https://api.github.com/users/{username}/repos')
            if response.status_code == 200:
                repos = response.json()
            else:
                repos = [{'name': f"Error: {response.json().get('message')}"}]
    else:
        form = UsernameForm()
    return render(request, 'github_app/list_repos.html', {'form': form, 'repos': repos})

6.urls.py (in github_app/)

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_repo, name='create_repo'),
    path('list/', views.list_repos, name='list_repos'),
]


7.urls.py (in github_api_project/)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('github/', include('github_app.urls')),
]


8.Templates
templates/github_app/create_repo.html
html
Copy
Edit
<h2>Create GitHub Repository</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>
<p>{{ message }}</p>


Run the Project

python manage.py runserver
