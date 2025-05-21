a=['nitin','nitin','rahul']
b=[i for i in a if i.startswith('n')]
print(b)

re=list(filter(lambda x :x.startswith("r"),a))
print(re)
word={}
char=[]
for i in a:
    if i in word:
        word[i]+=1
    else:
        word[i]=1
print("word is:", word)
for word,count in word.items():
    if count >1:
        char.append(word)
        char.append(count)
print("duplicate word is :",char)

def my_deco(func):
    def wrapper():

        print("im creating a decorator")

        func()

        print("we returned th efunction")
    return  wrapper
@my_deco
def atm():
    print("AT<")

atm()
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


class Parameter:
    def __init__(self,radius):
        self.radius=radius
        self.__name='nitin'

    def __str__(self):
        return f"my name is {self.__name}"
    def area(self):
        return 3.14 *self.radius*self.radius

    def circuferences(self):
        return 3.128*self.radius

    @staticmethod
    def statkit():
        print("we are static methid")

#radius=34
c=Parameter(radius=8)
print(c.circuferences())
print(c.area())
print(Parameter.statkit())
print(_Parameter__)




def comm_prefix(arr):
    min_arr=min(arr)
    max_arr=max(arr)
    commprefx=""
    len_min_arr=len(min_arr)

    for i in range(len_min_arr):
        if min_arr[i] ==max_arr[i]:
            commprefx+=min_arr[i]

        else:
            break

    return commprefx


arr=['fly','flt','flw']
print(comm_prefix(arr))


def ptest(arr):
    n=len(arr)+1
    t=n*(n+1)/2
    actual_sum=sum(arr)
    return t-actual_sum

arr=[2,4,5,1]
print(ptest(arr))

#ar=[3,4,6,1,4,7]
ar=[1,2,3,4]
is_sorted=True
for i in range(len(ar)-1):
    if ar[i] >ar[i+1]:
        is_sorted= False

if is_sorted:
    print("The table data is sorted.")
else:
    print(f"The table data is not sorted. The unsorted position is at index(1-based index).")

word=[2, 0, 4, 0, 3, 0, 5, 0]
result=[i for i in word if i%2==0 and i!=0] +[i for i in word if i%2 !=0] + [i for i in word if i ==0]

print("sorted result of dat is :",result)

def reverse_each_word(sentence):

    words= sentence.split(" ")
    rev_word=[word[::-1] for word in words]
    return " ".join(rev_word)  # Join words back with spaces

# Example usage:
print(reverse_each_word("abc de f"))

b="abc de f"
c= b[::-1]
print(c)