'''tests for platformTwitter'''

import pytest
from platformTwitter import Twitter
import configparser

file_name = ".test_config"
twet = Twitter(file_name)
keys = configparser.ConfigParser()

def test_initial_value():
    assert twet.name ==  "Twitter"
    assert twet.configfile == ".test_config"

def test_no_value():
    with pytest.raises(Exception):
        obj = Twitter()
        
    
@pytest.mark.skip(reason="let's fix it later")
def test_load_app_apikey():
    if twet.consumer_key == "XXXXX" :
        raise Exception("You haven't configured the API key. Please read Readme")
    if twet.consumer_secret == 'XXXXX':
            raise Exception("You haven't configured the API key. Please read Readme")
