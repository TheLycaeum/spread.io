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
