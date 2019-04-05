import webbrowser
import configparser
import tweepy
from platforms import Platform


class Twitter(Platform):
    "Platform for twitter"
    def __init__(self, filename):
        self.name = "Twitter"
        self.configfile = filename
        self.load()
        self.check_link()

    def check_link(self):
        "Check whether user is linked to twitter account or not"
        try:
            self.username = self.api.me().name
            self.is_linked = True
        except:
            self.is_linked = False

    def load(self):
        "Loads keys and api"
        consumer_key, consumer_secret = self.read_config()
        self.load_app_apikey(consumer_key, consumer_secret)
        self.load_user_key()
        self.api = tweepy.API(self.access)

    def load_app_apikey(self, consumer_key, consumer_secret):
        "Loads app api key"
        if consumer_key == "XXXXX" or consumer_secret == 'XXXXX':
            raise Exception("You haven't configured the API key. Please read Readme")
        else:
            self.access = tweepy.OAuthHandler(consumer_key,
                                              consumer_secret)

    def load_user_key(self):
        "Loads user access token"
        self.access.set_access_token(self.access_token,
                                     self.access_secret)
        self.url = self.access.get_authorization_url()

    def read_config(self):
        "Reads config file and store apikey values"
        config = configparser.ConfigParser()
        config.read(self.configfile)
        consumer_key = config['twitter_app']['consumer_key']
        consumer_secret = config['twitter_app']['consumer_secret']
        self.access_token = config['twitter_user']['access_token']
        self.access_secret = config['twitter_user']['access_secret']
        return (consumer_key, consumer_secret)

    def log_in(self):
        "Open the twitter in browser to authorize the app"
        webbrowser.open(self.url)

    def write_user_keys(self, pin):
        "Get access tokens using the PIN generated in browser"
        keys = self.access.get_access_token(pin)
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['twitter_user']['access_token'] = keys[0]
        config['twitter_user']['access_secret'] = keys[1]
        with open(self.configfile, 'w') as files:
            config.write(files)

    def delink(self):
        "Delink a user by removing config keys"
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['twitter_user']['access_token'] = "XXXXX"
        config['twitter_user']['access_secret'] = "XXXXX"
        with open(self.configfile, 'w') as files:
            config.write(files)

    def post(self, tweet):
        "Posts the tweet using api"
        try:
            self.api.update_status(tweet)
            self.post_status = True
        except:
            self.post_status = False
            raise Exception("Was Unable to post, check network connection")

