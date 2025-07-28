2.Requirements for Web Development Projects


Theory:
    
•Understanding project requirements.

Ans:-

Before starting any web development project, it's important to clearly understand what the
project aims to achieve. This includes:

1.Client Goals: What the client or user wants (e.g., a portfolio site, e-commerce platform, or booking system).

2.Target Audience: Who will use the website (age, interests, profession).

3.Core Features: What functionalities are needed (e.g., login system, product listing, payment gateway).

4.Technology Stack: What languages, frameworks, and tools will be used (e.g., HTML, CSS, JavaScript, Django).

5.Design Requirements: Layout, color scheme, branding, and user interface (UI/UX) preferences.

6.Budget and Time: Timeline for project completion and available resources.


•Setting up the environment and installing necessary packages. 
 
Ans:-

Before starting a web development project, it is important to prepare the development
environment. This ensures the project runs smoothly and all tools work together.

1. Setting Up the Environment:
    
Install a Code Editor: Use tools like Visual Studio Code, Sublime Text, or PyCharm.

Install Python: For Django or Flask projects, install Python (commonly version 3.8 or higher).


.Create a Virtual Environment:

python -m venv env

.Activating the Virtual Environment:

env\Scripts\activate


Lab: 
 
•Write a requirements.txt file for a Django project that includes all necessary dependencies. 
 
Ans:-

Django>=4.2,<5.0
djangorestframework>=3.14.0
mysqlclient>=2.2.0   
gunicorn             
python-decouple     
Pillow               
requests    


You can generate this file automatically after installing packages using:

pip freeze > requirements.txt

Practical Example:

2) Write a Python script to set up a Django project and install packages like django,
   djangorestframework, requests, etc.

ANS:-

import os
import subprocess


subprocess.run(["python", "-m", "venv", "env"])


subprocess.run(["env/Scripts/pip", "install", "django", "djangorestframework", "requests", "Pillow", "python-decouple"])


subprocess.run(["env/Scripts/django-admin", "startproject", "myproject"])

1.Create a virtual environment named env

2.Install required packages:

django

djangorestframework

requests

Pillow (for image upload)

python-decouple (for managing secret keys)
