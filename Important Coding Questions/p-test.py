# List2=[2,6,7,9,10]
# List1=[1,2,4,6,8]
# word = []
# for i in List1:
#     if i in List2:
#         word.append(i)
# print(word)
#
List2=[2,6,7,9,10]
min_elemnt=List2[0]
for i in List2:
    if i > min_elemnt:
        min_elemnt=i
print(min_elemnt)

#
# def fibb():
#     a,b=0,1
#     while True:
#         yield a
#         a,b =b,a+b
# f=fibb()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#

lower=int(input("enter lower number"))
upper=int(input("enter lower number"))

t=[]
for i in range(lower , upper+1):
    for j in range(2,i):
        if i %j ==0:
            break
    else:
        print(i)
# arr="today is friday"
# def revr_str(arr):
#     word=[]
#     for i in range(len(arr)-1,-1,-1):
#         word.append(arr[i])
#     return " ".join(word)
# arr1="today is friday"
# print(f"reverse word is {revr_str(arr1)}")
#
#
# def twosum(arr , target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+ arr[j]==target:
#                 print(f" the sum of two variable{arr[i]}, {arr[j]} is == {target}")
#     return target
# arr=[1,2,4,6,8]
# target=14
# print(twosum(arr , target))
#
#

# from selenium import  webdriver
# driver=webdriver.Chrome()
# driver.get("dummy rul")
# driver.find_element(By.ID,"refresh").click()

import  pytest

# class Runtest:
#     def test_twosum():
#         return "pass"
#
#
# r=Runtest()
# print(r.test_twosum())


def test_pass():
    name= "nitin"
    assert name==name