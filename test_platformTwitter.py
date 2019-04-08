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

def test_check_link():
    twet = Twitter(file_name)
    twet.check_link()
    assert twet.is_linked == False

def test_check_link_fail():
    twet = Twitter(file_name)
    
    config = configparser.ConfigParser()
    config.read(file_name)
    config['twitter_app']['consumer_key'] = 'Y22pLniUdwNsg5tg7B7UgFlnn'
    config['twitter_app']['consumer_secret'] = 'P85zJuLD7jBP1eW9EBZMjDbQkdVacljBni5y9gwd0qE5c13bWj'
    with open (file_name, 'w') as configfile:
        config.write(configfile)
    twet.load()
    twet.check_link()
    assert twet.is_linked == True
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['twitter_app']['consumer_key'] = 'XXXXX'
    reset['twitter_app']['consumer_secret'] = 'XXXXX'
    with open (file_name,'w') as config_file:
        reset.write(config_file)
    
def test_delink():
    twet = Twitter(file_name)
    reset = configparser.ConfigParser()
    reset.read(file_name)
    reset['twitter_app']['consumer_key'] = 'XXXXX'
    reset['twitter_app']['consumer_secret'] = 'XXXXX'
    with open (file_name,'w') as config_file:
        reset.write(config_file)
    twet.check_link()
    assert twet.is_linked == False

