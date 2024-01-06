from mastodon import Mastodon
from my_app.connections.streaming_api import establish_stream_connection
from flask import Flask, render_template, request, redirect, url_for, flash
from my_app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, migrate

from my_app.get_posts import post_to_dict

db = SQLAlchemy()
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) 
    
    app.config.from_object(Config)


    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.app_context()
    with app.app_context():
        db.init_app(app)
        # Creating an SQLAlchemy instance
        migrate = Migrate(app, db) # database migrations are used to keep the database up to date when new models are added or existing ones are changed
        db.create_all() # create the database if it doesn't already exist
        establish_stream_connection(app)
    
    from .models import User, Post

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    @app.route('/search')
    def search():
        from my_app.get_posts import get_all_posts
        search_term = request.args.get('term')
        # Perform any necessary search logic here
        # For example, you can use the 'search_term' to filter posts
        # and pass the filtered posts to the template
        posts = get_all_posts()[0]
        filteredPosts = []
        filteredPosts = [post for post in posts if 
                        isinstance(post.get('title'), str) and isinstance(post.get('text'), str) and
                        (search_term.lower() in post['title'].lower() or search_term.lower() in post['text'].lower())
                        ]
        return render_template('search_results.html', search_term=search_term, posts=filteredPosts)

    @app.route('/register')
    def register():
        return render_template("register.html")
    
    @app.route('/login')
    def login():
        return render_template("login.html")
    
    @app.route('/form')
    def form():
        return render_template("form.html")

    # THREE: multiple URL routes
    # @app.route('/')
    # @app.route("/projects/")
    # def projects():
    #     return 'The project page'

    # FOUR: errors with URL routes
    # @app.route("/about") # note the app route!
    # def about():
    #     return render_template('about.html')

    '''
    # CREATE
    @app.route("/user/toot/", methods=('GET', 'POST')) # this app route allows both GET and POST requests
    def toot_message():
        if request.method == 'POST': # do this only if a POST request is made
            title = request.form['title'] # get data via the request object
            content = request.form['content']

            if not title:
                flash('Title is required!')
            elif not content:
                flash('Content is required!')
            else: # if both title and content are provided, post to Mastodon
                m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")
                m.toot("Message title:"+title+"\nMessage content:"+content)
                return render_template('success.html') # render the success page
        
        return render_template('toot.html') # if a GET request is made, render the toot.html template

    # RETRIEVE
    @app.route("/user/timeline/<number>/")
    def timeline(number):
        if not number.isnumeric() or number > 100: # if the "number" parameter is not numeric or too large, set it to 10
            number = 10

        m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")
        timeline = m.timeline(timeline="local", limit=number) # get the user's local timeline
        print(timeline) # for debugging purposes, see console
        for toot in timeline: 
            content = toot['content']
            url = toot['url']
            account = toot['account']['username']
            print(account, content, url) # for debugging purposes, see console

        return render_template('timeline.html', timeline=timeline) # passing the timeline json object to the html template

    # UPDATE
    @app.route("/user/follow/", methods=('GET', 'POST'))
    def follow_user():
        if request.method == 'POST':
            # print(request)
            username = request.form['username'] # get the username from the request object
            pri'User.query.all() render_template('follow.html', username = None)

    # UPDATE 2
    @app.route("/user/follow_unfollow/", methods=('GET', 'POST'))
    def follow_unfollow_user():
        if request.method == 'POST':
            print(request.form)
            fstatus = request.form['fstatus'] # get the value of the fstatus radio button
            username = request.form['username'] # get the username from the request object
            
            m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")
            id = m.account_lookup(acct=username) # get the user's id (required to follow)
            if(fstatus == "follow"):
                m.account_follow(id)
            elif(fstatus == "unfollow"):
                m.account_unfollow(id)
                
            return render_template('follow_unfollow.html', username = username, fstatus = fstatus)
        
        return render_template('follow_unfollow.html', username = None)
    '''

    return app