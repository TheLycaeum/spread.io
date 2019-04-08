 # test_platformFacebook.py

import pytest
from platformFacebook import Facebook
import facebook as fb
import configparser

config = configparser.ConfigParser()
config['Facebook_client'] = {'client_id': '1234179660062675',
                             'client_secret': 'f04ef73cdaf8ecdcbfe536356ef31974',
                             'name':'spread'}

config['Facebook_user'] = {'access_token': 'EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD',
                           'page_name': 'Test'}
with open('/tmp/.test_config', 'w') as configfile:
    config.write(configfile)
    
file_name = "/tmp/.test_config"

def test_init_value():
    face = Facebook(file_name)
    assert face.name == "Facebook"
    assert face.configfile == "/tmp/.test_config"

def test_load_user_key():
    face = Facebook(file_name)
    access_token= face.load_user_key() 
    assert access_token  == 'EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD'

def test_check_link_True():
    face = Facebook(file_name)
    face.graph =fb.GraphAPI('EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD')
    face.check_link()
    assert face.is_linked == True

def test_check_link_False():
    face = Facebook(file_name)
    face.graph=fb.GraphAPI('XXXX')
    face.check_link()
    assert face.is_linked == False

def test_load_app_apikey():
    face = Facebook(file_name)
    config = configparser.ConfigParser()
    config.read(file_name)
    config['Facebook_client']['name'] = 'XXXXX' 
    with open(file_name, 'w') as configfile:
        config.write(configfile)
    with pytest.raises(Exception,match="You haven't configured the API keys. Please read README file"):
        face.load_app_apikey()
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['Facebook_client']['name'] = 'spread' 
    with open(file_name, 'w') as config_file:
        reset.write(config_file)

def test_token_from_url():
    face=Facebook(file_name)
    url='abc=Testgood&ok'
    access_token= face.get_token_from_url(url)
    assert access_token == 'Testgood'
    
def test_delink():
    face=Facebook(file_name)
    face.delink()
    assert face.is_linked == False
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['Facebook_user']['access_token'] = 'EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD'
    with open(file_name, 'w') as configfile:
        reset.write(configfile)

def test_authenticate_Page():
    face=Facebook(file_name)
    face.graph =fb.GraphAPI('EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD')
    keys = configparser.ConfigParser()
    keys.read(file_name)        
    keys['Facebook_user']['page_name']= 'Fail'
    with open(file_name, 'w') as config_file:
        keys.write(config_file)
    with pytest.raises(Exception,match=""):
        face.authenticate_page()
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['Facebook_user']['page_name'] = 'Test'
    with open(file_name, 'w') as configfile:
        reset.write(configfile)

def test_post_status_fail():
    face=Facebook(file_name)
    face.graph =fb.GraphAPI('XXXXX')
    status=face.post('Fail')
    assert status == False

def test_post_status_success():
    face=Facebook(file_name)
    face.graph =fb.GraphAPI('EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD')
    status=face.post('Do not panic: Successful test run')
    assert status == True
    


    
    
    

        
        
    
        
    


    
    
