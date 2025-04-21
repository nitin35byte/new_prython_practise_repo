l = 'akhiles'

# Convert the string to a list of characters
word = list(l)

# Initialize an empty stack
empty_stack = []

# Use a loop to reverse the characters using the stack
while word:
    empty_stack.append(word.pop())

# Print the stack which now contains the characters in reverse order
print(empty_stack)

# Optionally, if you want to convert it back to a string
reversed_string = ''.join(empty_stack)
print(reversed_string)



a = (2,3,[4,5],[3,6])
print(type(a))

a[2][0]=[1]
print(a)
total = 0
a = (2,3,[4,5],[3,6])
def sum_of_nested_list(item):
    total = 0
    for i in item:
        if isinstance(i , list):
            total +=sum_of_nested_list(i)
        else:
            total +=i
    return  total

a = (2,3,[4,5],[3,6])
print(sum_of_nested_list(a))


# class Car:
#
#     def __init__(self ,name , color):
#         self.name= name
#         self.color= color
#
#     def hondd(self , name , color , model):
#         self.name=name
#         self.color=color
#         self.model= model
#
#     def updated_version(self , honda):
#         pass
#
# obj = Car

# print(obj.hondd("civic", 'black', 2029))



# test = {'name':'Nitin' , 'age':27 ,'place':'Delhi', 'profession':'Softare engineer'}
# y=test.copy()
# print(test['name'])
# test['age']='25'
# print(test)
# test['employeer']='Protiviti consultacny'
# print(test)
#
# test.pop('age')
# print(test)
#
# for x in test.keys():
#     print(x)
# print(y.get('name'))


thisset = {"apple", "banana",'APPLE' ,"cherry"}
thisset_1 = {"apple", "banana",'APPLE' ,"cherry" , 'guava'}
for x in thisset:
  print(x)

if 'apple' in thisset:
    print("this is a good fruit to eat")
else:
    print('jaane de yarr')

thisset.add('watermelon')
print(thisset)

thisset.add('watermelon')
print(thisset)

thisset.discard('APPLE')
print(thisset)

print(thisset.difference(thisset_1))


set1=[1,2,3,4]
set2=[2,3,4,6]

a = set(set1)
b = set(set2)
print(a & b)
d = a.symmetric_difference_update(b)
print(d)

item = [x for x in a if x in b]
print(item)


import re

s = "fdsaf4sagtt6hrdhhj7gh9"
substrings = re.split(r'\d+', s)

print(substrings)
substrings.reverse()
print(substrings)

reversed_substring = substrings[::-1]
print(reversed_substring)  # Output: "olleh"


l = 'Automation'
l=l.lower()
seen = set()
unique = set()

for i in l:
    if i in seen:
        if i in unique:
            unique.remove(i)
    else:
        seen.add(i)
        unique.add(i)

uniq= ''.join(sorted(unique))
print(unique)

l = 'Automation'

seen = set()
unique = set()

for i in l:
    if i in seen:
        if i in unique:
            unique.remove(i)
    else:
        seen.add(i)
        unique.add(i)

unique_characters = ''.join(sorted(unique))
print(f"Unique characters: {unique_characters}")

s='I love conding very much'

stack = []

for i in s.split():
    stack.append(i)

rever=[]
while stack:
    for i in stack:
        rever.append(stack.pop())
print(word)


l = [1,2,3,4,5]

for i in range(len(l)-1,-1,-1):
    print(l[i])


def fib(num):
    a , b = 0 , 1
    while True:
        yield  a
        a ,b=b ,a+b

    return a , b

l=10
f = fib(l)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))