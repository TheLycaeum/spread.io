 # test_platformTwitter.py

import pytest
from platformTwitter import Twitter
import configparser
file_name = ".test_config"
twet = Twitter(file_name)
keys=configparser.ConfigParser()

def test_initial_value():
    assert twet.name ==  "Twitter"
    assert twet.configfile == ".test_config"

def test_no_value():
    with pytest.raises(Exception):
        obj = Twitter()
        
def test_read_config():
    keys.read(file_name)
    assert twet.consumer_key == 'Y22pLniUdwNsg5tg7B7UgFlnn'
    assert twet.consumer_secret == 'P85zJuLD7jBP1eW9EBZMjDbQkdVacljBni5y9gwd0qE5c13bWj'
    assert twet.access_token == '1112014959901175808-u77cU9I5dbT3NAhs5EboFKnxlSrtBf'
    assert twet.access_secret == 'HVsJWNoz0ozEZ9GOhypjpbX4N1URITl4dPNq4U9DgzWMz' 

def test_load_app_apikey():
    if twet.consumer_key == "XXXXX" :
        raise Exception("You haven't configured the API key. Please read Readme")
    if twet.consumer_secret == 'XXXXX':
            raise Exception("You haven't configured the API key. Please read Readme")
