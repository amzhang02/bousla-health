from mastodon import Mastodon
from flask import Flask
import requests
from flask_sqlalchemy import SQLAlchemy
from my_app.__init__ import create_app


#m = Mastodon(access_token="", api_base_url="https://social.cs.swarthmore.edu")

#m.toot("Test post via API using OAuth")

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SECRET_KEY'] = 'secretkey'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(80), nullable = False)

with app.app_context():
    db.create_all()