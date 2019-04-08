import abc

class  Platform(abc.ABC):

    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def load_app_apikey(self):
        pass

    @abc.abstractmethod
    def load_user_key(self):
        pass

    @abc.abstractmethod
    def check_link(self):
        pass

    @abc.abstractmethod
    def log_in(self):
        pass

    @abc.abstractmethod
    def write_user_keys(self, verifier):
        pass

    @abc.abstractmethod
    def delink(self):
        pass

    @abc.abstractmethod
    def post(self, message):
        pass
