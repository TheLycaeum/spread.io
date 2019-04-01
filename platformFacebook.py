import webbrowser
import facebook as f
from rauth import OAuth2Service
import rauth
import requests

def open_browser(url):
    '''Opens the authorize_url in web-browser'''
    webbrowser.open(url)

def get_url(params):
    '''Creates a authorize url for logining in facebook''' 
    url = facebook.get_authorize_url(**params)
    return url

def input_url_with_token():
    '''Takes the new url which holds the token and splits the string to get the access_token'''
    url_with_token=''
    url_with_token = input('After Granting permission please paste url Here:  ')
    access_tok=url_with_token.split('=')
    access_to=access_tok[1].split("&")
    access_token=access_to[0]
    return access_token

def get_api(cfg):
    '''gets the api object from GraphAPI'''
    page_access_token=None
    graph=f.GraphAPI(cfg['access_token'])
    response=graph.get_object('me/accounts')
    # fetching data attribute of response object
    for page in response['data']:
	#finding our page
        if page['id']==cfg['page_id']:
            page_access_token=page['access_token']
            graph=f.GraphAPI(page_access_token)
    return graph

def extend_token(cfg, client_id, client_secret):
    ''' Extend the expiration time of a valid OAuth access token.'''
    appi=get_api(cfg)
    extended_token = appi.extend_access_token(client_id, client_secret)
    return (extended_token['access_token'])

def post_message(cfg):
    '''Post a message in facebook page'''
    api=get_api(cfg)
    #print(dir(api))
    page_id=cfg['page_id']
    msg='Testing thru Oauth.!!!'
    
    #obj_call for posting text
    api.put_object("me", "feed", message=msg)
    
    #obj_call for posting image
    #api.put_photo(image=open('test.jpg', 'rb'), message='Test for uploading photo next is dp')
    #obj_call for posting dp
    #api.put_photo(image=open("jpeg_43.jpg", 'rb'), album_path=page_id + "/picture")  
    

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
    open_browser(url)
    access_token=input_url_with_token()
    cfg['access_token']=access_token
    extented_token=extend_token(cfg, client_id, client_secret)
    post_message(cfg)

    
    
if __name__=="__main__":
    facebook = OAuth2Service(name='spread',
                             client_id = '1234179660062675',
                             client_secret = 'f04ef73cdaf8ecdcbfe536356ef31974',
                             access_token_url='https://graph.facebook.com/oauth/access_token',
                             authorize_url='https://graph.facebook.com/oauth/authorize',
                             base_url='https://graph.facebook.com/')
    
    
    main()
