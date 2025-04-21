
# #string "Good morning"Count each character how many times its repeatedOutput should be in dictionary
#
#
str ='good morning'
b = ''.join(i for i in str if i.isalnum())

print(b)
fre={}

for i in b:
    if i in fre:

            fre[i]+=1
    else:
        fre[i]=1
print(fre)



# class Test:
#     def __init__(self ,a ,  b):
#         self.a=a
#         self.b=b
#     @staticmethod
#     def calcul():
#         c = a+b
#         print(c)
#
#
# t = test()
# t
#
#
# cl


def miss_no(arr):
    n=len(arr)+1
    c=n*(n+1)//2
    k=sum(arr)
    return c-k
arr=[1,2,4,5]
print(miss_no(arr))

def pk_test(arr):
    arr_set=set(arr)
    max_length=0
    word=[]
    for i in arr_set:
        if i -1 not in arr_set:
            current_max=1
            current_num=i
            current_word=[current_num]

            while current_num+1 in arr_set:
                current_max+=1
                current_num+=1
                current_word.append(current_num)

            if current_max>max_length:
                max_length=current_max
                word=current_word
    return max_length,word

arr=[2,4,3,5,7,8,2,55,7,72]
print(pk_test(arr))

