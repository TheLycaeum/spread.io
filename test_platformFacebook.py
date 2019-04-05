 # test_platformFacebook.py

import pytest
from platformFacebook import Facebook
import configparser

file_name = ".test_config"

def test_init_value():
    face = Facebook(file_name)
    assert face.name == "Facebook"
    assert face.configfile == ".test_config"

