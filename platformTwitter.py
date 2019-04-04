import webbrowser
import tweepy
from platforms import Platform
import configparser


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
        except :
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
        self.access.set_access_token(self.access_token,self.access_secret)


    def read_config(self):
        "Reads config file and store apikey values"
        keys=configparser.ConfigParser()
        keys.read(self.filename)
        self.consumer_key=keys['twitter_app']['consumer_key']
        self.consumer_secret=keys['twitter_app']['consumer_secret']
        self.access_token=keys['twitter_user']['access_token']
        self.access_secret=keys['twitter_user']['access_secret']
                  

    def log_in(self):
        "Open the twitter in browser to authorize the app"
        url = self.access.get_authorization_url()
        webbrowser.open(url)
        self.get_user_keys()
        self.write_user_keys()
        self.check_link() ###

    def get_user_keys(self):
        "Ask user to verify the PIN generated in browser"
        verifier = input('PIN: ').strip() ###
        self.keys = self.access.get_access_token(verifier)

    def write_user_keys(self):
        string = configparser.ConfigParser()
        string.read(self.filename)
        print()
        string['twitter_user']['access_token']=self.keys[0]
        string['twitter_user']['access_secret']=self.keys[1]
        with open(self.filename, 'w') as files:
            string.write(files)
            
    def post(self, tweet):
        "Posts the tweet using api"
        self.api.update_status(tweet)


def main():
    pluggin = Twitter(".config")
    while not pluggin.is_linked:
        pluggin.log_in()
    print(pluggin.is_linked)
    message = "Testing; app testing"
    status = pluggin.post(message)
    print(status)

if __name__ == '__main__':
    main()
