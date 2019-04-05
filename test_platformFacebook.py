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
    
    
