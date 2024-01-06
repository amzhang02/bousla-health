from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from my_app.db_helpers import add_comment_to_db,bring_awareness
from my_app.comment_mod import mod
main = Blueprint('main', __name__)
from flask_login import current_user, login_user

@main.route('/',methods=['GET', 'POST'])
@login_required
def dash():
    from my_app.get_posts import get_all_posts
    # Assuming the user is logged in and `current_user` is available
    if current_user.is_authenticated:
        username= ""
        user_id = current_user.get_id()
        username = current_user.name
    showWarn = 0
    comment = ""
    if request.method == 'POST':
        id = request.form.get('id')
        type = request.form.get('type')
        if type == "comment":
            # Retrieve the comment from the form
            comment = request.form.get('comment')
            warningShown = request.form.get('warn') == "warningShown"
            if (warningShown):
                # Call your Python function with the comment
                add_comment_to_db(username,id,comment)
                return redirect(url_for('main.dash'))
            else: 
                needsWarning = mod(comment)
                if needsWarning:
                    showWarn=id
                else:
                    add_comment_to_db(username,id,comment)
        if type =="awareness":
            bring_awareness(user_id,id)
            return redirect(url_for('main.dash'))
    posts,postsSortByTime,postsSortByEngagement,sexHealth,drug,alcohol,cancer,nutrition,fitness,prescriptions,vaccine,other = get_all_posts()
    return render_template("dashboard.html", posts=posts,postsSortByTime=postsSortByTime,postsSortByEngagement=postsSortByEngagement,sexHealth=sexHealth,drug=drug,alcohol=alcohol,cancer=cancer,nutrition=nutrition,fitness=fitness,prescriptions=prescriptions,vaccine=vaccine,other=other,userID= user_id,warningShown=showWarn,comment=comment)

#@main.route('/profile')
#def profile():
    #return 'Profile'

""" @main.route('/search')
#@login_required
def search():
    search_term = request.args.get('term')
    # Perform any necessary search logic here
    # For example, you can use the 'search_term' to filter posts
    # and pass the filtered posts to the template
    posts = get_all_posts()[0]
    filteredPosts = [post for post in posts if search_term.lower() in post['title'].lower() or search_term.lower() in post['text'].lower()]
    return render_template('search_results.html', search_term=search_term, posts=filteredPosts) """