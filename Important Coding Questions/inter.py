# lower = 1
# # upper = 33
# #
# # for i in range(lower, upper+1):
# #     for j in range(2,i):
# #         if i %j ==0:
# #             break
# #     else:
# #         print(i)
#
# # num=int(input("enter number"))
# # if num <1:
# #     print("please enter valid number")
# # elif num ==1:
# #     print(f"factorial of{num} is 1")
# # else:
# #     facto = 1
# #     for i in range(1,num+1):
# #         facto=facto*i
# #     print(facto)
#
# name="My Name is nitin"
# word="".join(i.lower().strip() for i in name if i.isalnum())
# w=[]
# dup=[]
# for i in word:
#     if i in w:
#         if i not in dup:
#             dup.append(i)
#     else:
#         w.append(i)
# #
# print(w)
# print(dup)
# # word = "Protiviti"
# # for i in range(20):
# #     print(word)

def miss_num(arr):
    n= len(arr)+1
    p=n*(n+1)//2
    tot_sum=sum(arr)
    return p-tot_sum
arr=[1,2,4,5]
print(miss_num(arr))

def missNumber(arr):
    miss=[]
    for i in range(arr[0],arr[-1]+1):
        if i not in arr:
            miss.append(i)
    return miss

arr=[1,3,5,7,9,11]
print(missNumber(arr))

def subtitle(arr,n):
    for i in range(0,len(arr),n):
        arr[i:i+n]=reversed(arr[i:i+n])
    return arr

arr=[1,2,3,4,5,6,7]
n=3
print(subtitle(arr,n))

def alteranate_rev(arr):
    word=arr.split()
    for i  in range(1,len(word),2):
        word[i]=word[i][::-1]
    return "".join(word)
input_string ="my name is nitin"
output = alteranate_rev(input_string)
print(output)

add=lambda a,b:a+b
print(add(2,3))