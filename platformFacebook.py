import webbrowser
import facebook as f
from rauth import OAuth2Service
import rauth
import requests


def get_url(params):
    '''Creates a authorize url for logining in facebook''' 
    url = facebook.get_authorize_url(**params)
    return url

def main():
    cfg={
        'page_id':'427579681383478',
	'access_token':''

        } 
    client_id = '1234179660062675'
    client_secret = 'f04ef73cdaf8ecdcbfe536356ef31974'
    redirect_uri = 'https://www.students.thelycaeum.in'
    params = {'scope': 'publish_pages',
              'response_type': 'token',
              'redirect_uri': redirect_uri}
    url=get_url(params)
    
    
if __name__=="__main__":
    facebook = OAuth2Service(name='spread',
                             client_id = '1234179660062675',
                             client_secret = 'f04ef73cdaf8ecdcbfe536356ef31974',
                             access_token_url='https://graph.facebook.com/oauth/access_token',
                             authorize_url='https://graph.facebook.com/oauth/authorize',
                             base_url='https://graph.facebook.com/')
    
    
    main()
