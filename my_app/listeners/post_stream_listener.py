from mastodon import StreamListener
from bs4 import BeautifulSoup
from my_app.connections.categorization_api import OpenAIClassifier
# Function that uses the BeautifulSoup library to convert html to text
def html_to_text(message):
    return str(BeautifulSoup(message,features="html.parser").get_text())
class PostStreamListener(StreamListener):
    """This is a listener class for the Mastodon Streaming API. 
       It extends the Mastodon class StreamListener and overrides two functions.

    Args:
        None
    """
    
    def on_update(self, status):
        #from .. import app
        from  .. import db
        from my_app import create_app
        from my_app.models import Post

        app = create_app()
        """This function executes code when a status is posted to Mastodon.
           It's called by the listener.

        Args:
            status (JSON): This is the status that was posted on Mastodon.
        """
        with app.app_context():
            existing_post = Post.query.filter_by(id=status['id']).first()
            if existing_post:
                print(f"Record with ID {status['id']} already exists.")
            else:
                classifier = OpenAIClassifier(app.config['OPENAI_API_KEY'])
                postText = html_to_text(status['content'])
                try:
                    postGeneratedCategory = classifier.get_category(postText)
                except Exception as e:
                    print("Failed to generate category. Error: " + str(e))
                    postGeneratedCategory = "other"
                receivedPost = Post(
                    id = status['id'],\
                    timeStamp = status['created_at'],\
                    url = status['url'],\
                    text = postText,\
                    replies_count = status['replies_count'],\
                    favourites_count = status['favourites_count'],\
                    account_id = status['account']['id'],\
                    account_username = status['account']['username'],\
                    comments = "[]",\
                    category = postGeneratedCategory,\
                    tags = "[]",\
                    engagement = 0,\
                    engagedUsers = "[]"\
                )
                print("Received a new post: ", receivedPost)
                db.session.add(receivedPost)
            # Commit the changes to the database
            db.session.commit()
            # code to write to the database should be included here
            """ receivedPost.id = status['id']
            receivedPost.text = status['content'] # this going to be in HTML; we need to parse it
            receivedPost.image = status['media_attachments'] # this is a list of media attachments; we need to convert 
            receivedPost.url = status['url']
            receivedPost.replies_count = status['replies_count']
            receivedPost.favourites_count = status['favourites_count']
            receivedPost.timeStamp = status['created_at']
            receivedPost.account_id = status['account']['id']
            receivedPost.account_username = status['account']['username'] """
    def on_status_update(self, status):
        """This function executes code when a status is updatd on Mastodon.
           It's called by the listener.

        Args:
            status (JSON): This is the status that was updated on Mastodon.
        """
        print("Received a new update: ", status)
        # code to write to the database should be included here, with
        # keeping in mind that a post already exists
