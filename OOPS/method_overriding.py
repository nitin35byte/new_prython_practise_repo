class Methodoverriding():

    def __init__(self , name , age):
        self.name=name
        self.age=age

    def baby(self):
        print("method overiing")

class Method(Methodoverriding):
    def __init__(self,name , age , location):
        super().__init__(name , age)
        self.location=location

    def baby(self):
        print("method test")

c=Method("nitin",29,"delhi")
print(c.name)
print(c.age)
print(c.location)