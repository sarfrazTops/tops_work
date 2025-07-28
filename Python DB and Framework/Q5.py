5. Virtual Environment

Theory:

• Understanding the importance of a virtual environment in Python projects.

Ans:-

A virtual environment in Python is an isolated workspace that allows you to manage dependencies for a specific project without affecting the global Python installation or other projects.


Project Isolation:
    
Each Python project can have its own set of libraries and dependencies. This prevents conflicts between projects.
For example, one project may need Django 3.2 while another needs Django 4.0 — both can coexist in separate environments.

Dependency Management:
Virtual environments make it easier to manage and control which packages and versions your project uses. You can easily install, upgrade, or remove packages without breaking other projects.

Avoids System Pollution:
Installing libraries globally (using pip install) can clutter your system Python environment and potentially break system tools that rely on Python.

Reproducibility:
You can create a requirements.txt file to list all your project’s dependencies. This allows others to recreate the same environment using pip install -r requirements.txt.

Security and Control:
You can test new packages in a safe, contained environment without risking the rest of your system or other projects.


• Using venv or virtualenv to create isolated environments.

Ans:-

venv:-Built-in module in Python 3.3+ to create virtual environments

virtualenv:-Third-party package; works with older versions of Python (including Python 2.x)
           and gives more flexibility

->How to Use

# Create virtual environment
python -m venv env_name

# Activate it
# Windows
env_name\Scripts\activate


# Install packages (isolated)
pip install django

# Save dependencies
pip freeze > requirements.txt

# Deactivate
deactivate

Lab:

• Set up a virtual environment for a Django project.


Set Up a Virtual Environment for a Django Project

Step 1: Create Project Directory

mkdir my_django_project
cd my_django_project


Step 2: Create a Virtual Environment

python -m venv env

Step 3: Activate the Virtual Environment
On Windows:

env\Scripts\activate



Step 4: Install Django

pip install django
You can verify the Django version:

django-admin --version


Step 5: Start a Django Project

django-admin startproject mysite
This creates a Django project named mysite.

Step 6: Run the Development Server

python manage.py runserver

Step 7: Freeze Requirements (Optional but recommended)

pip freeze > requirements.txt
This saves all the installed packages for future use (great for team projects or deployment).

Folder Structure

my_django_project/
│
├── env/                   ← Virtual environment folder
├── mysite/                ← Django project
│   ├── manage.py
│   └── mysite/
│       ├── settings.py
│       └── ...
├── requirements.txt       ← List of packages



Practical Example:


5) Write a Python program to create and activate a virtual environment,then install Django in it.



6. Project and App Creation
Theory:
• Steps to create a Django project and individual apps within the project.
• Understanding the role of manage.py, urls.py, and views.py.
Lab:
• Create a Django project with an app to manage doctor profiles.s





























