# a=[10,10]
# d=['a','b']
#
#
# r=[i for i in enumerate(a, start=5)]
# print(r)
# rsult=zip(a,d)
# print(list(rsult))
# k = {"name":"nitin", "age":12, "city":"Delhi"}
# values = ["Alice", 25, "New York"]
#
# person = dict(zip(k, values))
# print(person)
# word=[]
# for keyy ,value in k.items():
#     word.append([keyy , value])
# print(word)

emp_list= [('Ankit' , 10000) , ('Nitin',12000) , ('Rahul' , 15000) , ('Sumit' , 14000) , ('Dheeraj' , 21000) , ('Pavan' , 11000) , ('Mohit' , 13000)]
l=sorted(emp_list, key=lambda item: item[1] , reverse=True)
print(l)

r=dict(emp_list)
print(r)
total=0
for value , salary in emp_list:
    total=total+salary
average=total/len(emp_list)
print(average)
print(total)
jaada=[]
for value , salary in emp_list:
    if salary > average:
        jaada.append([value,salary])

print(jaada)
sorte_jaada=sorted(jaada)
print(sorte_jaada)
is_sorted=True
for i in range(len(sorte_jaada)-1):
    if sorte_jaada[i] >sorte_jaada[i+1]:
        is_sorted=False

if is_sorted:
    print('data is sorted')
else:
    print("not sorted")

def comm_pr(arr):
    max_arr=max(arr)
    min_arr=min(arr)
    commm_prefix=""
    len_comm=0
    en_min_arr=len(min_arr)

    for i in range(en_min_arr):
        if min_arr[i] ==max_arr[i]:
            commm_prefix+=min_arr[i]
            len_comm+=1
        else:
            break

    return commm_prefix ,len_comm

arr=["fly","flt" ,"flu" , "flu"]

print(comm_pr(arr))


def consecutive(arr):
    arr_set=set(arr)
    max_length=0
    word=[]

    for char in arr_set:
        if char-1 not in arr_set:
            current_num=char
            current_length=1
            current_word=[current_num]

            while current_num +1 in arr_set:
                current_num+=1
                current_length+=1
                current_word.append(current_num)

            if current_length >max_length:
                max_length=current_length
                word=current_word

    return word , max_length

arr=[2,3,4,5,6,88,89 , 87 , 90]
print(consecutive((arr)))

def longest_substring(arr):
    freq={}
    word=""
    start=0
    max_length=0

    for char in range(len(arr)):
        if arr[char] in freq and freq[arr[char]] >=start:
            start=freq[arr[char]]+1
        freq[arr[char]]=char

        current_max=char-start+1
        if current_max> max_length:
            max_length=current_max
            word=arr[start:char+1]

    return word , max_length

arr="bhgijfsdethe"
print(longest_substring(arr))


def mis_number(arr):
    miss=[]
    for i in range(arr[0] , arr[-1] +1):
        if i not in arr:
            miss.append(i)
    return miss

arr=[1,2,4,6,8,9,11]
print(mis_number(arr))


class Person:

    def __init__(self,name):
        self.name=name

    def personal_info(self,age,location):
        self.age=age
        self.location=location


    def __str__(self):
        return f"my age is {self.name} my age is {self.age} and i'm from {self.location}"

class Identification(Person):
    #
    # def __init__(self,id):
    #     self.id=id

    def id_info(self,id_number):
        self.id_number=id_number

    def __str__(self):
        return f"{self.id_number}"

id=Identification("rahul")
id.personal_info(30, "Delhi")
id.id_info("12NCHH546")
print(id)
print(id.age)
print(id.location)
print(id.name)


class Interview:
    def __init__(self,role):
        self.role=role

    def interview_mode(self,mode):
        self.mode=mode


    def __str__(self):
        return f"{self.role},{self.mode}"

class Full_data(Interview):

    def get_alldata(self,mode,interviewr_name):
        super().interview_mode(mode)
        self.interviewr_name=interviewr_name

    def __str__(self):
        return f"interview mod is {self.mode} and the interviewr is {self.interviewr_name}"


f=Full_data("softwaredeveloper")

f.get_alldata("online","rahul")
print(f)


class Protiviti:

    def __init__(self,c_name):
        self.c_name=c_name

    def parent(self,parent_name):
        self.parent_name=parent_name


class Data(Protiviti):

    def full_data(self,tp):
        self.tp=tp


    def parent(self,parentData):
        self.parentData=parentData
        print("data data")

    def __str__(self):
        return f"Company: {self.c_name}, Parent: {getattr(self, 'parentData', 'N/A')}"

d=Data("protivit",)

d.parent("Roberthalf")
print(d)


name="nitin chadhary"

word =name.replace(" ","")
print(word)
char1=word[:7][::-1]
char2=" "
char3=word[7:][::-1]
print(char1+char2+char3)
