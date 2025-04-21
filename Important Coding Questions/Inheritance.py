class Phone():

    def __init__(self , price , brand  , camera):
        print("I have a iphone ")
        self.price = price
        self.brand = brand
        self.camera = camera

    def description(self):
        print("I am polumorphism")

class smartphone(Phone):
    def __init__(self ,price , brand , camera , os , ram):
        print("Ios  have few more functionality")
        super().__init__(price, brand , camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone cunstructor")

    def description(self):
        print("I am polumorphism 2")

s= smartphone(2000000 , 'Apple' , '50mp' ,'ios', 128 )
s.description()

print(s.os , s.ram , s.brand , s.camera ,s.price)