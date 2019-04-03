from appWindow import *
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



def main():
    app = Spread()

    names = app.plugin_names()
    appwin = Display(names)
    # print(names)

if __name__ == '__main__':
    main()
