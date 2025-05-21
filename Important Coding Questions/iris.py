class Person:

    def __init__(self,name):
        self.name= name

    def dictt(self,age):
        self.age=age

    def __str__(self):
        return f"{self.age}"

class Child(Person):

    def child_1(self ,age, classs):
        self.classs = classs
        super().dictt(age)


    def __str__(self):
        return f"{self.classs}"


c=Child("rahul")
print(c.child_1(3 , 34))
print(c)
print(c.age)
a = "This is a test. Test this."

b=a.lower().split()
d=[i for i in a if a.isalnum()]
c={}

for i in d:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
word = "".join(i for i in a if a.isalnum())
print(word)

fre={}
for i in a:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

print(fre)


a = "This is a test. Test this."

# Convert to lowercase and remove punctuation
words = [word.strip(".").lower() for word in a.split()]

# Count word occurrences
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

a=[53,73,43,8,54,4,6,2]
max_element=a[0]
second_max_element=a[0]


for i in a:
    if i >max_element:
        second_max_element=max_element
        max_element=i
    elif i>second_max_element and i <max_element:
        second_max_element=i

print(max_element)
print(second_max_element)