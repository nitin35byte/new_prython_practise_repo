class Person:

    def __init__(self,name):
        self.name=name

    def dictt(self,age):
        self.age=age

class Child(Person):

    def child_1(self,age , location):
        self.location=location
        super().dictt(age)

    def __str__(self):
        return f"{self.age} {self.location}"

c=Child("rahul")
c.child_1("24" ,"delhi")
print(c)

a = "This is a test. Test this."
char=[char.strip(".").lower() for char in a.split()]
print(char)

word_count = {}
for c in char:
    if c in word_count:
        word_count[c] += 1
    else:
        word_count[c] = 1

print(word_count)


def twosum(arr,target):
    counter=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                counter+=1
                print(arr[i]+arr[j])

    return arr , counter


a=[2,3,5,8,9,5,4]
target=7
print(twosum(a,target))

def sumtarget(arr,target):
    counter=0
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i] +arr[j]==target:
                print(arr[i], arr[j])
                counter+=1
    return arr , counter
arr=[1,2,3,7,4,5,6]
target=7
print(sumtarget(arr , target))


class Protiviti:

    def __init__(self , location):
        self.location=location


    def addres(self,city , state , pincode):
        self.city=city
        self.state=state
        self.pincode=pincode

    def __str__(self):
        return f"city is {self.city} and state is {self.state} and pincode is {self.pincode}"


class Candidate(Protiviti):

    def addres(self,city ,state ,pincode , district):
        super().addres(city , state , pincode)
        self.district=district

    def __str__(self):
        return f"City: {self.city}, District: {self.district}, State: {self.state}, Pincode: {self.pincode}"

c = Candidate("Delhi")
c.addres("New Delhi", "Delhi", "110001", "Central Delhi")
print(c)

def two_sum(arr,target):
    counter=0
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i]+ arr[j]==target:
                counter+=1
                print(f"sum of: {arr[i] , arr[j]}==target :{target}")
    return arr  ,counter
arr=[2,4,5,6,1,3]
target=7
print(two_sum(arr , target))


def consecutive(arr):
    arr_set=set(arr)
    max_length=0
    char=""
    total=0
    for i in arr_set:
        if i-1 not in arr_set:
            current_char=i
            current_max=1
            current_word=[current_char]
            i_total=current_char

            while current_char+1 in arr_set:
                current_char+=1
                current_max+=1
                current_word.append(current_char)
                i_total=i_total+current_char

            if current_max >max_length:
                max_length=current_max
                char=current_word
                total=i_total

    return max_length  , char , total

arr=[2,3,5,7,5,99,87,98,97,96]
print(consecutive(arr))

def longest_sube(arr):
    start=0
    max_length=0
    word=""
    char_gre={}

    for i in range(len(arr)):
        if arr[i] in char_gre and char_gre[arr[i]] >= start:
            start=char_gre[arr[i]]+1
        char_gre[arr[i]]=i


        current_max=i-start+1
        if current_max> max_length:
            max_length=current_max
            word=arr[start:i+1]

    return max_length , word

arr="bghdfserus"
print(longest_sube(arr))

upper=1
lower=20
for i in range(lower , upper+1):
    for j in range(2 , i):
        if i%j==0:
            break
    else:
        print(i)

a="2a4u5t7omation"
total=0
word_count=[]
for i in a:
    if i.isdigit():
        total=total+int(i)
    else:
        word_count.append(i)
print(total)
print("".join(word_count)+str(total))


a = "This is a test. Test this."
char=[i.strip(".").lower() for i in a.split()]
t={}
for i in char:
    if i in t:
        t[i]+=1
    else:
        t[i]=1

print(t)
p=[]
for value in char:
    if t[value]==1:
        p.append(value)
        break

print(p)

def rev_word(arr):
    word=arr.split()
    for i in range(0, len(word) , 2):
        word[i]=word[i][::-1]
    return "".join(word)

input_string ="my name is nitin"
output = rev_word(input_string)
print(output)
