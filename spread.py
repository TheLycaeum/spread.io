from appWindow import *
from platformTwitter import *
from platformFacebook import *


config_file = ".config"

class Spread():

    def __init__(self):
        self.get_plugins()
    
    def get_plugins(self):
        self.plugins = []
        self.plugins.append(Twitter(config_file))
        self.plugins.append(Facebook(config_file))

    def plugin_names(self):
        names = []
        for plug in self.plugins:
            names.append(plug.name)
        return names



if __name__ == '__main__':
    app = Spread()
    names = app.plugin_names()
    print(names)
