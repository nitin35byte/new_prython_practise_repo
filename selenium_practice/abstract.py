from abc import ABC , abstractmethod
class Myclass(ABC):
    @abstractmethod
    def decortaor(self):
        print("under application")

    def security(self):
        pass

class Class2(Myclass):
    def functools(decorator):
        print("under static")

    def security(self):
         print("security inherited")

c=Class2()
c.functools()
c.security()
c.decortaor()