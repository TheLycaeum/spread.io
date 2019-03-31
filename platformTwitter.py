import tweepy
import webbrowser
import time


consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
def get_url():
    # get access token from the user and redirect to auth URL
    auth_url = auth.get_authorization_url()
    return auth_url
    
def open_browser(url):
    """open the url on browser"""
    webbrowser.open(url)
    time.sleep(1)

def get_key_and_secret():
    # ask user to verify the PIN generated in broswer
    verifier = input('PIN: ').strip()
    touple_of_keys = auth.get_access_token(verifier)
    list_of_keys = list(touple_of_keys)
    return list_of_keys

def post_tweet(list_of_keys):
    """post tweet using api"""
    key = list_of_keys[0]
    secret = list_of_keys[1]
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    username = api.me().name
    print("Welcome ", username)
    time.sleep(.5)
    tweet =input("Tweet here: " ) # toDo 
    api.update_status(tweet)

