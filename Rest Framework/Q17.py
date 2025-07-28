17.Twitter API Integration 

Theory:

•Using Twitter API to fetch and post tweets, and retrieve user data. 

Ans:-

What is the Twitter API?

The Twitter API allows developers to programmatically interact with Twitter data. This includes:

Reading tweets and user information

Posting tweets on behalf of users

Searching hashtags, trends, and mentions

Managing timelines, likes, followers, and more

-There are two major versions of the Twitter API:

v1.1 (legacy but still in use for some features)

v2 (modern, more structured, and preferred for new applications)


-Posting a Tweet
To post a tweet using Twitter API v2, you must use OAuth 2.0 with user context.

Endpoint (v2):

POST https://api.twitter.com/2/tweets


Example Request (using bearer token and OAuth2 user access):

{
  "text": "Hello Twitter API from my app!"
}


Fetching Tweets
To read tweets, you can use the recent search endpoint or user timeline endpoint.

Example: Search Recent Tweets

GET https://api.twitter.com/2/tweets/search/recent?query=python


Example: Get Tweets from a User

GET https://api.twitter.com/2/users/{user_id}/tweets


Retrieving User Data
To get info about a specific user:

Endpoint:

GET https://api.twitter.com/2/users/by/username/{username}


Example Response:

{
  "data": {
    "id": "12345678",
    "name": "Sarfraz Khan",
    "username": "sarfraz_dev"
  }
}


 
Practical Example:

17) Write a Django project to fetch and display the latest 5 tweets from a Twitter user using
    the Twitter API.

Ans:-

1.Create Project and App

django-admin startproject twitter_project
cd twitter_project
python manage.py startapp twitter_app


2.settings.py
Add 'twitter_app' to INSTALLED_APPS.

3.forms.py

from django import forms

class TwitterUserForm(forms.Form):
    username = forms.CharField(label='Twitter Username', max_length=100)

4.views.py

from django.shortcuts import render
import requests
from .forms import TwitterUserForm

# Replace with your Bearer Token from Twitter Developer Portal
BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'

HEADERS = {
    'Authorization': f'Bearer {BEARER_TOKEN}'
}

def get_tweets(request):
    tweets = []
    error = None

    if request.method == 'POST':
        form = TwitterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            # Step 1: Get user ID
            user_url = f'https://api.twitter.com/2/users/by/username/{username}'
            user_response = requests.get(user_url, headers=HEADERS)

            if user_response.status_code == 200:
                user_id = user_response.json()['data']['id']

                # Step 2: Get user's latest 5 tweets
                tweet_url = f'https://api.twitter.com/2/users/{user_id}/tweets?max_results=5'
                tweet_response = requests.get(tweet_url, headers=HEADERS)

                if tweet_response.status_code == 200:
                    tweets = tweet_response.json().get('data', [])
                else:
                    error = "Failed to fetch tweets."
            else:
                error = "User not found."
    else:
        form = TwitterUserForm()

    return render(request, 'twitter_app/get_tweets.html', {'form': form, 'tweets': tweets, 'error': error})

5.urls.py (in twitter_app/)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tweets, name='get_tweets'),
]

6.urls.py (in twitter_project/)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twitter_app.urls')),
]


7.get_tweets.html

<!DOCTYPE html>
<html>
<head>
    <title>Fetch Tweets</title>
</head>
<body>
    <h2>Enter Twitter Username</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Get Tweets</button>
    </form>

    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    {% if tweets %}
        <h3>Latest Tweets:</h3>
        <ul>
            {% for tweet in tweets %}
                <li>{{ tweet.text }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>


Run the Project

python manage.py runserver
