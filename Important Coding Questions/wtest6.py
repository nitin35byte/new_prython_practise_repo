# # #
# # # 1. click on element
# # # 2. validate textwrap
# #
# # click element
# # Get element text
# # Hover
# #
# # IF      ${i}    INRANGE    ${element}
# # RUN keyword ANd Check   IF        ${element}      is      Visisble
#
# a = 'automation testing'
# # a = a.split()
# b = []
# for i in range(len(a)-1 , -1  ,-1):
#     b.append(a[i])
#
# print(''.join(b))
#
# word = {}
#
# for i in a:
#     if i in word:
#         word[i]+=1
#     else:
#         word[i]=1
#
# print(word)

# abcabcabcbd
def substring(arr):
    start=0
    max_lenght=0
    word = ""
    frequency={}

    for char in range(len(arr)):
        if arr[char] in frequency and frequency[arr[char]] >= start:
            start = frequency[arr[char]]+1
        frequency[arr[char]]=char

        current_max=char-start+1
        if current_max > max_lenght:
            max_lenght =current_max
            word = arr[start: char+1]

    return word
arr='abcabcabcbd'
p=(substring(arr))
print(p)
#
#
# arr='abcabcabcbd'
# print(arr[1:4])
#
#
# post  ,put patch

# create wbdriver
# open link
# from selenium import webdriver
# driver=webdriver.chrome()
# driver.get("gmail.com")
# data=driver.find_element(By.ID ,'test').send_keys('test')
# data.clear

with open("test.txt",'w') as f:
    f.write("my name is nitin\n"
            "i m from delhi")
    # f.close()

with open("test.txt","r") as f:
    print(f.readline())

file=open("test_1.txt","w")
file.write("i have a onterview today with tcs")
f=open("test_1.txt","r")
print(f.readline())

from itertools import permutations, combinations, combinations_with_replacement

word = "rahul"

# Generate all permutations
perm = [''.join(p) for p in permutations(word)]
print("Permutations:", perm)