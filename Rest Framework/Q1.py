Introduction to APIs 
 
Theory: 
 
•What is an API (Application Programming Interface)?

Ans:-

In Django, an API (Application Programming Interface) is a way to allow different
 applications or clients (like web, mobile apps, etc.) to interact with your Django project,
 usually by exchanging data over the internet.

•Types of APIs: REST, SOAP.

1. REST (Representational State Transfer)

Ans:-

-REST is a popular web API style.

-It uses standard HTTP methods like GET, POST, PUT, DELETE.

-Data is usually exchanged in JSON or XML format.

-REST APIs are simple, scalable, and easy to use.



2. SOAP (Simple Object Access Protocol)

Ans:-

SOAP is a protocol-based API.

It uses XML format for messages.

It works over multiple protocols like HTTP, SMTP.

More secure and strict than REST, but also more complex.


•Why are APIs important in web development?

Ans:-

APIs (Application Programming Interfaces) play a crucial role in modern web development.
They allow different software systems to communicate and share data, making web applications
more powerful, flexible, and scalable.

Reasons Why APIs Are Important:

1.Data Sharing Between Systems

APIs allow websites and applications to exchange data easily (e.g., a weather app gets
real-time data from a weather API).

2.Connect Frontend and Backend

APIs connect the frontend (React, Angular, mobile app) with the backend (like Django)
to fetch or send data.

3.Third-Party Integrations

APIs help add features like:

Google Maps

Paytm or Razorpay for payments

Social logins (Google, Facebook)


4.Reusability
Once an API is created, it can be reused in multiple apps (web, mobile, desktop).

5.Security
APIs provide a secure way to access only specific data or services, without exposing internal code or databases.

6.Faster Development
APIs save time by using ready-made services instead of building everything from scratch.


Lab: 
 
•Write a Python program that consumes a simple public API (e.g., a joke API).


import requests

# Public API URL to get a random joke
api_url = "https://official-joke-api.appspot.com/random_joke"

# Sending a GET request to the API
response = requests.get(api_url)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()  # Converting JSON to Python dictionary
    print("Here is a joke for you:")
    print("Question:", data['setup'])         # Printing the setup
    print("Answer:", data['punchline'])       # Printing the punchline
else:
    print("Could not fetch joke. Please try again later.")

Output:-

Here is a joke for you:
Question: Why did the scarecrow win an award?
Answer: Because he was outstanding in his field!


Practical Example: 
 
1.Write a Python script to fetch a random joke from an API and display it on the console.


import requests


api_url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(api_url)


if response.status_code == 200:
   
    joke = response.json()

   
    print("Here's a random joke for you:\n")
    print(" ", joke['setup'])
    print(" ", joke['punchline'])
else:

    print("Failed to fetch a joke. Please try again later.")

 


