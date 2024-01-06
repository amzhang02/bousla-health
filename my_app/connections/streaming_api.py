from mastodon import Mastodon
from my_app.listeners.post_stream_listener import PostStreamListener 
def establish_stream_connection(app):
    mastodon = Mastodon(
    access_token = app.config['ACCESS_TOKEN'], 
    api_base_url= 'https://social.cs.swarthmore.edu'
    )
    listener = PostStreamListener()
    tag = 'BouslaHealthCheck'
    Mastodon.stream_hashtag(mastodon, tag, listener, local=False, run_async=True, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
