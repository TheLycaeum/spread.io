import webbrowser
import configparser
import tweepy
from platforms import Platform


class Twitter(Platform):
    "Platform for twitter"

    def __init__(self, filename):
        self.name = "Twitter"
        self.configfile = filename


    def load(self):
        "Loads keys and api"
        self.read_config()
        self.load_app_apikey()
        self.load_user_key()
        self.api = tweepy.API(self.service)
        self.check_link()

    def read_config(self):
        config_dict = dict()
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config_dict.update({"consumer_key" :config['twitter_app']['consumer_key']})
        config_dict.update({"consumer_secret" : config['twitter_app']['consumer_secret']})
        config_dict.update({"access_token" : config['twitter_user']['access_token']})
        config_dict.update({"access_secret": config['twitter_user']['access_secret']})
        return config_dict

    def load_app_apikey(self):
        "Loads app api key"
        config_dict = self.read_config()
        if config_dict['consumer_key'] == "XXXXX" or config_dict['consumer_secret'] == 'XXXXX':
            raise Exception("You haven't configured the API keys. Please read README file.")
        else:
            self.service = tweepy.OAuthHandler(config_dict['consumer_key'],
                                               config_dict['consumer_secret'])

    def load_user_key(self):
        "Loads user access token"
        "Loads user access token"
        config_dict = self.read_config()
        self.service.set_access_token(config_dict['access_token'],
                                      config_dict['access_secret'])
        self.url = self.service.get_authorization_url()

    def check_link(self):
        "Check whether user is linked to twitter account or not"
        try:
            username = self.api.me().name
            self.is_linked = True
        except:
            self.is_linked = False

    def log_in(self):
        "Open the twitter in browser to authorize the app"
        webbrowser.open(self.url)

    def write_user_keys(self, verifier):
        "Get access tokens using the verifier-PIN generated in browser"
        keys = self.service.get_access_token(verifier)
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
        self.is_linked = False


    def post(self, message):
        "Posts the tweet using api"
        try:
            self.api.update_status(message)
            post_status = True
        except:
            post_status = False
            #raise Exception("Was Unable to post, check network connection")
        return post_status




