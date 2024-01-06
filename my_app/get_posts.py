from mastodon import Mastodon

def post_to_dict(post):
    return {
        'title': "title",
        'text': post.text,
        'image': "img",
        'url': post.url,
        'comments': post.comments,
        'category': post.category,
        'tags': post.tags,
        'engagement': post.engagement,
        'timeStamp' : post.timeStamp,
        'id' : str(post.id),
        'url' : post.url,
        'replies_count' : post.replies_count,
        'favourites_count' : post.favourites_count,
        'account_id' : post.account_id,
        'account_username' : post.account_username,
        'engagedUsers': post.engagedUsers
    }

def get_all_posts():
    from .models import Post
    posts = Post.query.all()
    posts = [post_to_dict(post) for post in posts]
    # Sorting by the timeStamp attribute
    postsSortByTime = sorted(posts, key=lambda x: x['timeStamp'])
    postsSortByTime.reverse()
    # Sorting by the enagement attribute (assuming it's an integer)
    postsSortByEngagement = sorted(posts, key=lambda x: x['engagement'], reverse=True)

    # Creating a new list with posts of category "SexHealth"
    sexHealth = [post for post in posts if post['category'] == "sexHealth"]

    # Creating a new list with posts of category "alcohol"
    alcohol = [post for post in posts if post['category'] == "alcohol"]

    # Creating a new list with posts of category "drug"
    drug = [post for post in posts if post['category'] == "drug"]

    # Creating a new list with posts of category "cancer"
    cancer = [post for post in posts if post['category'] == "cancer"]

    # Creating a new list with posts of category "nutrition"
    nutrition = [post for post in posts if post['category'] == "nutrition"]

    # Creating a new list with posts of category "fitness"
    fitness = [post for post in posts if post['category'] == "fitness"]

    # Creating a new list with posts of category "prescriptions"
    prescriptions = [post for post in posts if post['category'] == "prescriptions"]

    # Creating a new list with posts of category "vaccine"
    vaccine = [post for post in posts if post['category'] == "vaccine"]

    # Creating a new list with posts of category "prescriptions"
    other = [post for post in posts if post['category'] == "other"]
    return posts,postsSortByTime,postsSortByEngagement,sexHealth,drug,alcohol,cancer,nutrition,fitness,prescriptions,vaccine,other