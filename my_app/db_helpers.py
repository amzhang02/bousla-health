def add_comment_to_db(username,id,comment):
    from .models import Post
    from . import db
    post_to_update = Post.query.get(id)
    if post_to_update:
        comments =post_to_update.comments
        if(comments and comments == "[]"):
            newComments= "[['"+username + "','" +comment+"']]"
        else:
            newComments = comments[:comments.rfind(']')] + ",['"+username+"','" + comment + "']]"
        post_to_update.comments = newComments
        db.session.commit()

def bring_awareness(userID,id):
    from .models import Post
    from . import db
    post_to_update = Post.query.get(id)
    engagedUsers = post_to_update.engagedUsers
    if(engagedUsers):
        if(not (userID in eval(engagedUsers))):
            if(engagedUsers == "[]"):
                engagedUsers = "['"+userID+ "']" 
            else:
                engagedUsers = engagedUsers[:engagedUsers.index(']')] + ",'" + userID + "']"
    else:
        engagedUsers = "['"+id+ "']"
    post_to_update.engagedUsers = engagedUsers
    engagement=post_to_update.engagement +1
    post_to_update.engagement = engagement
    db.session.commit()