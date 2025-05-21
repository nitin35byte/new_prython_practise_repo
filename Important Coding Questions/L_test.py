## Create dictionary and update country and gender
d={"name":"Niitn" , "age":27}
c={"location":"Niitn" , "pd":27}
d.update(country="India" ,gender="male")
d.update(c)
print(d)
#remove age from dictionary
d.pop("age")
print(d)

#Convert dictionary to list
d={"name":"Niitn" , "age":27}
d.update(country="India" ,gender="male")
word=[]
for key, value in d.items():
    word.append([key,value])

print(word)
#
#count frequenct of element
l = [1,2,3,4,1,2,3,4,1,2,1,2,3,4]
fre={}
duplicate=[]

for i in l:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

print(fre)
cha="Hi Nitin how are you?"
#remove duplicate from list
word=[]
duplicate=[]

for i in cha:
    if i in word:
        duplicate.append(i)
    else:
        word.append(i)

print(f"duplicate values is : {duplicate}")
print(word)

#predict output
l1 = [1, 2, 3]
l2 = [4, 5, 6]
r=[x * y for x in l1 for y in l2]
#r=4,10,18
print(r)

#reverse the word
s = "INTERVIEW"
rev=[]
for i in range(len(s)-1,-1,-1):
    rev.append(s[i])

print("".join(rev))

#create decorator and how to use it
def my_decor(func):
    def wrapper():
        print("i m creating custom decorator")

        func()

        print("in a decor ")

    return wrapper
@my_decor
def decor_test():
    print("checkoing decorator")

decor_test()

#write api snipper valdate error code and response body
import requests
#def test_login():
    # base_url="https://www.amazon.in/"
    # header="test data"
    #
    # response=requests.get(base_url)
    # assert response.status_code==200
    # assert response.json()["title"]=="Mr"


#create inheritance -inherit parent class,  , method overiding
class Interview:

    def __init__(self,company):
        self.company=company

    def car_name(self, name , color):
        self.name= name
        self.color=color

class Owner(Interview):
    #
    # def __init__(self):
    #     pass

    def owner_detail(self, ow_name , number):
        self.ow_name=ow_name
        self.number=number

    # def car_name(self, name, color):
    #     self.name = name
    #     self.color = color

    def car_name(self,brand):
        self.brand = brand

    def __str__(self):
        return f"{self.brand}"

o=Owner("honda")
o.car_name("tesla")
print(o)

d1={"a":20,"b":30}
d2={"a":20,"b":30}
d1.update(d2)
print(d1)


