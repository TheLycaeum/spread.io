import webbrowser
import time
import tweepy
from platform import Platform

class Twitter(Platform):
    "Platform for twitter"

    def load_app_apikey(self):
        "Loads app api key"
        consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.access = tweepy.OAuthHandler(consumer_key, consumer_secret)

    def log_in(self):
        """open the url on browser"""
        url = self.access.get_authorization_url()
        webbrowser.open(url)
        time.sleep(1)
        self.get_key_and_secret()

    def get_key_and_secret(self):
        "ask user to verify the PIN generated in broswer"
        verifier = input('PIN: ').strip()
        touple_of_keys = self.access.get_access_token(verifier)
        list_of_keys = list(touple_of_keys)
        return list_of_keys

    def post(self, list_of_keys):
        "post tweet using api"
        key = list_of_keys[0]
        secret = list_of_keys[1]
        self.access.set_access_token(key, secret)
        api = tweepy.API(self.access)
        username = api.me().name
        print("Welcome ", username)
        time.sleep(.5)
        tweet = input("Tweet here: ")
        api.update_status(tweet)
