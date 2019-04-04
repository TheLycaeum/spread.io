import webbrowser
import configparser
import tweepy
from platforms import Platform


class Twitter(Platform):
    "Platform for twitter"
    def __init__(self, filename):
        self.name = "Twitter"
        self.filename = filename
        self.load()
        self.check_link()

    def check_link(self):
        "Check whether user is linked to twitter account or not"
        try:
            self.username = self.api.me().name
            self.is_linked = True
        except:
            self.is_linked = False
            # raise Exception("Error occured")

    def load(self):
        "Loads keys and api"
        self.read_config()
        self.load_app_apikey()
        self.load_user_key()
        self.api = tweepy.API(self.access)

    def load_app_apikey(self):
        "Loads app api key"
        if self.consumer_key == "XXXXX" or self.consumer_secret == 'XXXXX':
            raise Exception("You haven't configured the API key. Please read Readme")
        else:
            self.access = tweepy.OAuthHandler(self.consumer_key,
                                              self.consumer_secret)

    def load_user_key(self):
        "Loads user access token"
        self.access.set_access_token(self.access_token,
                                     self.access_secret)

    def read_config(self):
        "Reads config file and store apikey values"
        file = configparser.ConfigParser()
        file.read(self.filename)
        self.consumer_key = file['twitter_app']['consumer_key']       ## Should remove from instance
        self.consumer_secret = file['twitter_app']['consumer_secret'] ##
        self.access_token = file['twitter_user']['access_token']
        self.access_secret = file['twitter_user']['access_secret']

    def log_in(self):
        "Open the twitter in browser to authorize the app"
        url = self.access.get_authorization_url()
        webbrowser.open(url)

    def write_user_keys(self, pin):
        "Get access tokens using the PIN generated in browser"
        keys = self.access.get_access_token(pin)
        file = configparser.ConfigParser()
        file.read(self.filename)
        file['twitter_user']['access_token'] = keys[0]
        file['twitter_user']['access_secret'] = keys[1]
        with open(self.filename, 'w') as files:
            file.write(files)

    def post(self, tweet):
        "Posts the tweet using api"
        self.api.update_status(tweet)
