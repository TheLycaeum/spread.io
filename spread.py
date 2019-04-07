from platformTwitter import *
from platformFacebook import *


config_file = ".config"

class Spread():

    def __init__(self):
        self.get_plugins()
    
    def get_plugins(self):
        "Plugin all platforms"
        self.plugins = []
        self.plugins.append(Twitter(config_file))
        self.plugins.append(Facebook(config_file))
        return self.plugins

    def load_platforms(self):
        "Loads all platforms"
        for plug in self.plugins:
            plug.load()
    
    def check_linked(self):
        "Checks if plugins are linked"
        linked = []
        for plug in self.plugins:
            if plug.is_linked:
                linked.append(plug)
        return linked
