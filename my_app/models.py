from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Post(db.Model):
# id : Field which stores unique id for every post in database table
# created_at: Date and time at which the post was created
# URL: URL for the post
# replies_count: Number of replies for the post
# favourites_count: Number of favourites for the post
# account_id: User ID of the account which posted the post
# account_username: Username of the account which posted the post
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    timeStamp = db.Column(db.DateTime, unique=False, nullable=False)
    url = db.Column(db.String(2048), unique=False, nullable=False)
    text = db.Column(db.String(1000), unique=False, nullable=False)
    replies_count = db.Column(db.Integer, unique=False, nullable=False)
    favourites_count = db.Column(db.Integer, unique=False, nullable=False)
    account_id = db.Column(db.String(), unique=False, nullable=False)
    account_username = db.Column(db.String(), unique=False, nullable=False)

    # stored data from Bousla Web
    # comments: comments from Bousla web serialized as a string
    comments = db.Column(db.String(), unique=False, nullable=False)
    category = db.Column(db.String(), unique=False, nullable=False)
    tags = db.Column(db.String(), unique=False, nullable=False)
    engagement = db.Column(db.Integer, unique=False, nullable=False)
    engagedUsers = db.Column(db.String(), unique=False, nullable=True, default="[]")


    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"ID: {self.id}, URL: {self.url}, Content: {self.text}, num_replies: {self.replies_count}, num_favourites: {self.favourites_count}, account_id: {self.account_id}, account_username: {self.account_username} \
        num_favorites: {self.favourites_count}, account_id: {self.account_id}, account_username: {self.account_username}, comments = {self.comments}, category : {self.category}, tags : {self.tags}, engagement : {self.engagement}, Engaged Users:{self.engagedUsers}"


