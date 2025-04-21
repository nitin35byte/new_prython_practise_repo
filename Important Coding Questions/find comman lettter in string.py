def common_letter():
    # string_1=input("enter first string")
    # string_2 = input("enter second string")
    string_1='nitin'
    string_2="nitish"
    s1=set(string_1)
    s2 = set(string_2)
    s3=s1 & s2

    print(s3)
    # lst= s1.intersection(s2)
    lst2=s1.difference(s2)
    # lst3=s1.union(s2)
    # lst4=s1.issubset(s2)
    # print("common letters are :","".join(lst))
    #
    print("unions are :",lst2)

common_letter()



a = "akhilesh"
b = "rajesh"
c =""
for i in a:
    if i in b:
        c +=i
print("code is :",c)
print("".join(set(c)))


## frequency of wordt
# text_1= input("enter word")
# word = text_1.split()
#
# d={}
# for i in text_1:
#     if i not in d.keys():
#         d[i]=0
#         d[i]=d[i] +1
# print(d)

## List to dictionary

a =[1 ,2 ,3,4 ]
b=['n , w , r , t , y']
result=dict(zip(a, b))
print(b)
text_1= 'hello world'
d={}
for i in text_1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)