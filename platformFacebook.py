import webbrowser
import configparser
from platforms import Platform
from rauth import OAuth2Service
import facebook as fb


class Facebook(Platform):
    "Platform for Facebook"

    def __init__(self, filename):
        self.name = "Facebook"
        self.configfile = filename
        self.load()
        self.check_link()

    def check_link(self):
        "Checks whether user is linked to facebook account or not"
        key = configparser.ConfigParser()
        key.read(self.configfile)
        self.access_token=key['Facebook_user']['access_token']
        try:
            graph = fb.GraphAPI(self.access_token)
            response = graph.get_object('me')  
            self.username = response['name']
            self.is_linked = True
        except :
            self.is_linked = False

    def log_in(self):
        "Open the facebook in browser to authorize the app"
        params = {'scope': 'publish_pages',
                  'response_type': 'token',
                  'redirect_uri': 'https://www.students.thelycaeum.in'}
        url = self.service.get_authorize_url(**params)
        webbrowser.open(url)

    def write_user_keys(self, url):
        "Writes the access_token to .config file"
        self.get_token_from_url(url)
        self.extend_token()

        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['Facebook_user']['access_token'] = self.access_token['access_token']
        with open(self.configfile, 'w') as configfile:
            config.write(configfile)

    def delink(self):
        "Delinks the platform"
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['Facebook_user']['access_token'] = 'XXXXX'
        with open(self.configfile, 'w') as configfile:
            config.write(configfile)


    def get_token_from_url(self, url):
        "Gets access token from redirect url"
        self.access_token = url.split('=')[1].split('&')[0]
        
    def extend_token(self):
        "Extend the expiration time of a valid OAuth access token."
        graph = fb.GraphAPI(self.access_token)
        self.access_token = graph.extend_access_token(self.client_id,
                                                      self.secret)

    def load(self):
        "Loads keys and api"
        self.read_config()
        self.load_app_apikey()
                
    def read_config(self):
        "Reads the .config file"
        keys = configparser.ConfigParser()
        keys.read(self.configfile)        
        self.page_name=keys['Facebook_user']['page_name']
        self.app_name = keys['Facebook_client']['name']
        self.client_id = keys['Facebook_client']['client_id']
        self.secret = keys['Facebook_client']['client_secret']
        self.access_token= keys['Facebook_user']['access_token']

    def load_app_apikey(self):
        "Loads app api key"
        if self.app_name == 'XXXXX' or self.client_id == 'XXXXX' or self.app_name=='XXXXX':
            raise Exception("You haven't configured the API keys, please read README file")
        else:
            self.service = OAuth2Service(name=self.app_name,
                                         client_id=self.client_id,
                                         client_secret=self.secret,
                                         access_token_url='https://graph.facebook.com/oauth/access_token',
                                         authorize_url='https://graph.facebook.com/oauth/authorize',
                                         base_url='https://graph.facebook.com/')

    def post(self,message):
        " Checks the Page is authentic and then Posts the message in facebook page"
        # self.graph=fb.GraphAPI(self.access_token)
        self.post_status= False
        key = configparser.ConfigParser()
        key.read(self.configfile)
        self.access_token=key['Facebook_user']['access_token']
        graph = fb.GraphAPI(self.access_token)
        try:
            response = graph.get_object('me/accounts')
            self.post_status = True
        except:
            self.post_status = False
            raise Exception("Was Unable to post, check network connection")

        for page in response['data']:
	    #finding if the page is granted permission and obtaining its page_token
            if page['name'] == self.page_name:
                page_token = page['access_token']
                self.graph = fb.GraphAPI(page_token)
            else:
                raise Exception("Cant find page in permission list")
        self.graph.put_object("me", "feed", message=message)
            
if __name__ == '__main__':
    pluggin = Facebook('.config')
    message = 'This works i hope !'
    if pluggin.is_linked:
        pluggin.post(message)
        pass
    else:
        pluggin.log_in()
        pluggin.post(message)

  
