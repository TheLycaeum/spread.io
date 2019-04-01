import webbrowser
import time
import tweepy
from platform import Platform

class Twitter(Platform):
    "Platform for twitter"

    def __init__(self, app_file, user_file):
        self.app_file = app_file
        self.user_file = user_file


    def load(self):
        "Loads keys and api"
        self.load_app_apikey()
        self.load_user_key()
        self.api = tweepy.API(self.access)
        self.status = self.api.verify_credentials()

    def load_app_apikey(self):
        "Loads app api key"
        consumer_key, consumer_secret = self.read_config(self.app_file)
        if consumer_key == "XXXXX" or consumer_secret == 'XXXXX':
            raise Exception("You haven't configured the API key. Please read Readme")
        else:
            self.access = tweepy.OAuthHandler(consumer_key,
                                              consumer_secret)

    def load_user_key(self):
        "Loads user access token"
        self.keys = self.read_config(self.user_file)
        self.access.set_access_token(self.keys[0],
                                     self.keys[1])


    def read_config(self, filename):
        "Reads config file and store apikey values"
        with open(filename) as file:
            lines = file.read()
            item = lines.split('\n')
            key = item[0].split('=')[1].strip()
            secret =  item[1].split('=')[1].strip()
            return key, secret


    def log_in(self):
        "Open the twitter in browser to authorize the app"
        url = self.access.get_authorization_url()
        webbrowser.open(url)
        time.sleep(1)
        self.get_user_keys()
        self.write_user_keys(self.user_file)

    def get_user_keys(self):
        "Ask user to verify the PIN generated in browser"
        verifier = input('PIN: ').strip()
        self.keys = self.access.get_access_token(verifier)

    def write_user_keys(self, user_file):
        string = " Key = {} \n Secret = {}".format(str(self.keys[0]),
                                                   str(self.keys[1]))
        with open(user_file, 'w') as file:
            file.write(string)


    def post(self):
        "post tweet using api"
        username = self.api.me().name
        print("Welcome ", username)
        time.sleep(.5)
        tweet = input("Tweet here: ")
        self.api.update_status(tweet)


def main():
    pluggin = Twitter(".config_twitter_app",".config_twitter_user")
    try:
        pluggin.load()
        if pluggin.status:
            print(True)
        else:
            print(False)
    except:
        print(None)

if __name__ == '__main__':
    main()
