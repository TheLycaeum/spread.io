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

