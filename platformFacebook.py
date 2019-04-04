import webbrowser
from platforms import Platform
from rauth import OAuth2Service
import facebook as fb
import configparser


class Facebook(Platform):
    "Platform for Facebook"

    def __init__(self, filename):
        self.name = "Facebook"
        self.configfile = filename
        self.load()
        self.check_link()
        

    def check_link(self):
        "Checks whether user is linked to twitter account or not"
        key = configparser.ConfigParser()
        key.read(self.configfile)
        self.access_token=key['Facebook_user']['access_token']
        try:
            graph = fb.GraphAPI(self.access_token)
            response = graph.get_object('me')  
            self.username = response['name']
            #print("Logged in as: ", self.username)
            self.is_linked = True
        except :
            self.is_linked = False
            #raise Exception("Not linked")

    def log_in(self):
        "Open the facebook in browser to authorize the app"
        params = {'scope': 'publish_pages',
                  'response_type': 'token',
                  'redirect_uri': 'https://www.students.thelycaeum.in'}
        url = self.service.get_authorize_url(**params)
        webbrowser.open(url)

    def get_token_from_url(self):
        "Gets access token from redirect url"
        url_with_token = input('After Granting permission please paste url Here:  ')
        self.access_token = url_with_token.split('=')[1].split('&')[0]
        self.extend_token()
        
    def extend_token(self):
        "Extend the expiration time of a valid OAuth access token."
        # Not sure whether a return value is required here
        graph = fb.GraphAPI(self.access_token)
        self.access_token=graph.extend_access_token(self.client_id, self.secret)
        #print(self.access_token['access_token'])
        config = configparser.ConfigParser()
        config.read(self.configfile)
        config['Facebook_user']['access_token']= self.access_token['access_token']
        with open(self.configfile, 'w') as configfile:
            config.write(configfile)

    def load(self):
        "Loads keys and api"
        self.read_config()
        self.load_app_apikey()
                
    def read_config(self):
        "Reads the .config file"
        keys = configparser.ConfigParser()
        keys.read(self.configfile)        
        self.page_name=keys['Facebook_user']['page_name']
        #427579681383478 and name is Test
        self.app_name = keys['Facebook_client']['name']
        #'spread'# should be in config
        self.client_id = keys['Facebook_client']['client_id']
        #'1234179660062675'                      
        self.secret = keys['Facebook_client']['client_secret']
        #'f04ef73cdaf8ecdcbfe536356ef31974'
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
        key = configparser.ConfigParser()
        key.read(self.configfile)
        self.access_token=key['Facebook_user']['access_token']
        graph = fb.GraphAPI(self.access_token)
        response = graph.get_object('me/accounts')
        #import pdb; pdb.set_trace()
        #print(response)
        for page in response['data']:
	    #finding if the page is granted permission and obtaining its page_token
            if page['name'] == self.page_name:
                page_token = page['access_token']
                self.graph = fb.GraphAPI(page_token)
        self.graph.put_object("me", "feed", message=message)
        print("Posted")

if __name__ == '__main__':
    pluggin = Facebook('.config')
    message = 'This works i hope !'
    if pluggin.is_linked:
        pluggin.post(message)
        pass
    else:
        pluggin.log_in()
        pluggin.post(message)
        
  
