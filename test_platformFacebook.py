 # test_platformFacebook.py

import pytest
from platformFacebook import Facebook
import configparser

file_name = ".test_config"

def test_init_value():
    face = Facebook(file_name)
    assert face.name == "Facebook"
    assert face.configfile == ".test_config"

def test_read_config():
     face = Facebook(file_name)
     assert face.page_name  == 'Test'
     assert face.client_id  == '1234179660062675'
     assert face.secret =='f04ef73cdaf8ecdcbfe536356ef31974'

def test_write_user_keys():
    face=Facebook(file_name)
    assert face.access_token == 'XXXXX'

def test_token_from_url():
    face=Facebook(file_name)
    url='abc=Testgood&ok'
    face.get_token_from_url(url)
    assert face.access_token == 'Testgood'

def test_delink():
    face=Facebook(file_name)
    face.delink()
    assert face.access_token == 'XXXXX'

def test_post_Page_check():
    face=Facebook(file_name)
    config = configparser.ConfigParser()
    config.read(file_name)
    config['Facebook_user']['access_token'] = 'EAARietg6H9MBAG8yjTeQYZC1uJqQGFvZCpmnQCzrxZBhILZChMRUohQlgZCrtEySOHyZCEyeVnNguZBU42fRZBPZCAjlObC3sIxaQwKLfbljw6Wu4WWZAOd7og3sxSmkBzKgrlg0h2PpADUeovympZAQX12xnEOsrhFjLYZD' 
    with open(file_name, 'w') as configfile:
        config.write(configfile)       
    keys = configparser.ConfigParser()
    keys.read(file_name)        
    face.page_name=keys['Facebook_user']['page_name']
    face.post("Testing")
    assert face.page_status == True
    #reseting .test_config
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['Facebook_user']['access_token'] = 'XXXXX'
    with open(file_name, 'w') as configfile:
        reset.write(configfile)


        
        
    
        
    


    
    
