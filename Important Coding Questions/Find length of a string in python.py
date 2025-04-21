

def findLen(str):
    counter = 0
    for i in str:
        counter+=1
    return  counter

str='nitin'
print(findLen(str))


class test_class():

    def __init__(self , name , age):
        self.name=name
        self.age=age

obj=test_class("rahul" , 28)
print(obj.age)
print(obj.age)


def subList(arr):
    total=0
    for i in arr:
        if isinstance(i   , list):
            total+=subList(i)

        else:
            total+=i
    return total

print(subList())