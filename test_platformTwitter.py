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

def test_load_app_apikey():
    twet = Twitter(file_name)
    config = configparser.ConfigParser()
    config.read(file_name)
    config['twitter_app']['consumer_key'] = 'XXXXX'
    with pytest.raises(Exception, match="You haven't configured the API keys. Please read README file."):
        twet.load_app_apikey()

