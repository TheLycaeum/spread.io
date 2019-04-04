import abc

class  Platform(abc.ABC):

    @abc.abstractmethod
    def load_app_apikey(self):
        pass
    
    @abc.abstractmethod
    def log_in(self):
        pass

    @abc.abstractmethod
    def post(self):
        pass
