from flask import Flask
from datetime import datetime


app = Flask(__name__)
welcomeView = 0
dateView = 0

@app.route("/")
def welcome():
    return "Welcome to my flash application!"


@app.route("/date")
def date():
    global dateView
    dateView += 1
    return "This page was served at " + str(datetime.now()) + " and viewed " + str(dateView) + " times"
