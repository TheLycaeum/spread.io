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

    def plugin_names(self):
        "Gets name of all plugged-in platforms"
        names = []
        for plug in self.plugins:
            names.append(plug.name)
        return names

    def check_linked(self):
        "Checks if plugins are linked"
        linked = []
        for plug in self.plugins:
            if plug.is_linked:
                linked.append(plug)
        return linked

    def log_in(self, plugin):
        "Logs in the respective plugin to retrive access_token"
        plugin.log_in()

    def post(self, plugin,message):
        "Post the message to the respective plugin"
        plugin.post(message)
