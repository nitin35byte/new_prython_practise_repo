# class Employee:
#
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.__salary=salary
#
#
#     def __str__(self):
#         return f"my name is {self.name} and my age is {self.age}my i m earning {self.__salary}"
#
#
#     def get_salary(self):
#         return self.__salary
#
# s=2300000
# a=('Nitin' , '25', '2500000')
# c=Employee('Nitin' , '25', '2500000')
# print(c)
# salary=c.get_salary()
# print(salary)


def subsequencies(arr):
    arr_set=set(arr)
    max_length=-0
    word=[]

    for char in arr_set:
        if char-1 not in arr_set:
            current_char=char
            current_length=1
            currentword=[current_char]

            while current_char+1 in arr_set:
                current_char+=1
                current_length+=1
                currentword.append(current_char)

            if current_length > max_length:
                max_length=current_length
                word=currentword

    return word , max_length

a = [1,5,3,7,8,2,8]
print(subsequencies(a))


def longest_substring(arr):
    word=''
    char_frequency={}
    start=0
    max_length=0

    for char in range(len(arr)):
        if arr[char] in char_frequency and char_frequency[arr[char]] >=start:
            start=char_frequency[arr[char]]+1

        char_frequency[arr[char]]=char


        current_max=char-start+1
        if current_max > max_length:
            max_length=current_max
            word=arr[start:char+1]

    return word , max_length

arr="abcabcbb"
print(longest_substring(arr))


def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
bubblesort(arr)
print("Sorted array t:", bubblesort(arr))


def duplicatee(arr):
    arr="".join(i for i in arr if i.isalnum() )
    char={}
    duplicate=[]

    for i in arr:
        if i in char:
            char[i]+=1
        else:
            char[i]=1

    for char , count in char.items():
        if count >1:
            duplicate.append(char)

    return duplicate

arr='my name is nitin'
print(f"duplicet character are {duplicatee(arr)}")