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
        self.plugins.append(Twitter('.config'))  #for testing changed Twitter(config_file) to Twitter('.config')
        self.plugins.append(Facebook('.config')) #for testing changed Facebook(config_file) to Facebook('.config')

    def plugin_names(self):
        "Gets name of all plugged-in platforms"
        names = []
        for plug in self.plugins:
            names.append(plug.name)
        return names
     def check_linked(self, plugin):
        "Checks if plugin is linked"
        #the plugin arg should be Twitter/Facebook(config_file) 
        status=False
        plugin.check_link()
        status=plugin.is_linked
        return status

    def log_in(self, plugin):
        "Logs in the respective plugin to retrive access_token"
        plugin.log_in()

    def post(self, plugin,message):
        "Post the message to the respective plugin"
        plugin.post(message)
  
def main():
    app=Spread()
    app.get_plugins()
    #print(app.plugins)
    #import pdb; pdb.set_trace()
    #The below is just for testing and shows how to call funtions
    # twitter_status=app.check_linked(app.plugins[0])
    # facebook_status=app.check_linked(app.plugins[1])
    # print(twitter_status, '\n', facebook_status)

    names = app.plugin_names()
    appwin = Display(names)
    # print(names)
    
if __name__ == '__main__':
    main()
