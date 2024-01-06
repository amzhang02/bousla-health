# Bousla Health Checker
Contributors: Alyssa Zhang, Andrew Henin, Belle Romea

## Features
* Account creation with basic Django Authentication
* Fetch posts from Mastodon with hashtag (BouslaHealthCheck) for in-app dashboard
* Commenting and liking fetched posts inside Bousla app
* Categorize and filter posts using [ChatGPT API](https://openai.com/product)
* Comment moderation with [Perspective API](https://perspectiveapi.com/)

## VERY IMPORTANT: DO NOT SKIP
**If you're a contributor,** please make sure to run the following command and push before you merge your Pull Request.
```
pip freeze > requirements.in && pip-compile
```

**If you're a user,** please make sure to run the following command before using the app to install the needed dependencies.
```
pip install -r requirements.txt
``` 

## Common commands:
1. To run the Flask app, run the following command.
```
flask --app my_app run --debug --port 8000
```
2. To run tests, run the following command.
```
python3 run_tests.py
```

## Installation:

1. Install virtualenv:
`pip3 install virtualenv`
   
2. Create your virtual environment:
   `virtualenv venv`

3. Actrive your virtual environment:
   `source venv/bin/activate`

4. Install Mastodon, Flask and its dependencies within your virtual environment:
   `pip3 install Mastodon.py`
   `pip3 install flask`

5. Create a file called "user_token" in the main directory. Add your user authentication token to this file, e.g., "asdf4348sdgaj4r". This will allow you to access your Mastodon account from the app. Note that it is added to the .gitignore file so you don't accidentally push it to GitHub.