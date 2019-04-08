import webbrowser
import configparser
from rauth import OAuth2Service
import facebook as fb
from platforms import Platform


class Facebook(Platform):
    "Platform for Facebook"

    def __init__(self, filename):
        self.name = "Facebook"
        self.configfile = filename


    def load(self): # pragma: no cover
        "Loads keys and api"
        self.load_app_apikey()
        access_token = self.load_user_key()
        self.graph = fb.GraphAPI(access_token)
        self.check_link()

    def load_app_apikey(self):
        "Loads app api key"
        keys = configparser.ConfigParser()
        keys.read(self.configfile)
        app_name = keys['Facebook_client']['name']
        client_id = keys['Facebook_client']['client_id']
        client_secret = keys['Facebook_client']['client_secret']

        #? Do we need to check page_name here?
        if app_name == 'XXXXX' or client_id == 'XXXXX' or client_secret == 'XXXXX':
            raise Exception("You haven't configured the API keys. Please read README file.")
        else:
            self.service = OAuth2Service(name=app_name,
                                         client_id=client_id,
                                         client_secret=client_secret,
                                         access_token_url='https://graph.facebook.com/oauth/access_token',
                                         authorize_url='https://graph.facebook.com/oauth/authorize',
                                         base_url='https://graph.facebook.com/')

    def load_user_key(self):
        "Loads user access token"
        keys = configparser.ConfigParser()
        keys.read(self.configfile)
        access_token = keys['Facebook_user']['access_token']
        return access_token

    def check_link(self):
        "Checks whether user is linked to facebook account or not"
        try:
            response = self.graph.get_object('me')
            username = response['name']
            self.is_linked = True
        except:
            self.is_linked = False


    def log_in(self):# pragma: no cover
        "Open the facebook in browser to authorize the app"
        params = {'scope': 'publish_pages',
                  'response_type': 'token',
                  'redirect_uri': 'https://www.students.thelycaeum.in'}
        url = self.service.get_authorize_url(**params)
        webbrowser.open(url)

    def write_user_keys(self, verifier):# pragma: no cover
        "Writes the access_token to .config file"
        access_token = self.get_token_from_url(verifier)
        exd_token = self.extend_token(access_token)

        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['Facebook_user']['access_token'] = exd_token['access_token']
        with open(self.configfile, 'w') as configfile:
            config.write(configfile)

    def get_token_from_url(self, url):
        "Gets access token from redirect url"
        splitter = url.split('=')[1].split('&')[0]
        return splitter

    def extend_token(self, access_token):# pragma: no cover
        "Extend the expiration time of a valid OAuth access token."
        keys = configparser.ConfigParser()
        keys.read(self.configfile)
        client_id = keys['Facebook_client']['client_id']
        client_secret = keys['Facebook_client']['client_secret']

        graph = fb.GraphAPI(access_token)
        exd_token = graph.extend_access_token(client_id,
                                              client_secret)
        return exd_token


    def delink(self):
        "Delinks the platform"
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['Facebook_user']['access_token'] = 'XXXXX'
        with open(self.configfile, 'w') as configfile:
            config.write(configfile)
        self.is_linked = False


    def authenticate_page(self):
        "Checks the Page is authentic"
        response = self.graph.get_object('me/accounts')

        keys = configparser.ConfigParser()
        keys.read(self.configfile)
        page_name = keys['Facebook_user']['page_name']

        for page in response['data']:
	#finding if the page is granted permission and obtaining its page_token
            if page['name'] == page_name:
                page_token = page['access_token']
                self.graph = fb.GraphAPI(page_token)
            else:
                raise Exception("Cant find page in permission list")

    def post(self, message):
        "Posts the message using api"
        try:
            self.authenticate_page()
            self.graph.put_object("me", "feed", message=message)
            post_status = True
        except:
            post_status = False
            #raise Exception("Was Unable to post, check network connection")
        return post_status
