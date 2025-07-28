17.	GitHub Project Deployment 
 
Theory: 
 
•Steps to push a Django project to GitHub. 

ANS:-

1.Create a GitHub repository

Go to https://github.com

Click on New Repository and give it a name.

2.Initialize Git in your Django project folder

git init

3.Add all project files to Git

git add .

4.Commit the files

git commit -m "Initial commit"

5.Connect your local project to GitHub

git remote add origin https://github.com/your-username/your-repo-name.git

6.Push your project to GitHub

git push -u origin main


Lab: 
 
•Deploy a Django project to GitHub for version control.

1.Open Terminal / CMD
Navigate to your Django project directory:

cd path/to/your/django/project

2.Initialize Git

git init

3.Create a .gitignore file
Add this content to avoid uploading unnecessary files:

__pycache__/
db.sqlite3
*.pyc
*.log
env/


4.Add all files to Git

git add .

5.Commit the files

git commit -m "Initial Django project commit"

6.Create a repository on GitHub

Go to https://github.com

Click New Repository, name it, and don’t add a README.

7.Connect local Git to GitHub

git remote add origin https://github.com/your-username/your-repo-name.git

8.Push code to GitHub

git push -u origin main

 
Practical Example:

17) Write a step-by-step guide to deploying the “Doctor Finder” project to GitHub.

Step 1: Open Terminal and Navigate to Project

cd path/to/DoctorFinder

Step 2: Create a .gitignore File
This file tells Git which files/folders to ignore.
Create a .gitignore file and add:

__pycache__/
*.pyc
*.log
db.sqlite3
.env
/static/
media/
env/

Step 3: Initialize Git

git init

Step 4: Add All Files to Git

git add .

Step 5: Commit the Files

git commit -m "Initial commit of Doctor Finder project"

Step 6: Create a Repository on GitHub
Go to https://github.com

Click New Repository

Name it doctor-finder

Do not add README or .gitignore (you already have one locally)

Click Create Repository

Step 7: Connect Local Git to GitHub

git remote add origin https://github.com/your-username/doctor-finder.git


Step 8: Push Project to GitHub

git branch -M main
git push -u origin main
