from abc import  abstractmethod , ABC

class Banking(ABC):

    def database(self):
        print("we are handling atabse")
    @abstractmethod
    def security(self):
        print('add me')


class Login(Banking):

    def login(self):
        print("we are login to banking application")


    def security(self):
        print('security add me')
l = Login()
l.login()
l.security()
l.database()