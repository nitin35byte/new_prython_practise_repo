lower= int(input("enter he upper number"))
upper= int(input("enter he lower number"))

for i in range(lower , upper+1):
    for j in range(2 , i):
        if i % j== 0:
            break
    else:
        print(i)


from collections import Counter
d1={"a":20,"b":30}
d2={"a":20,"b":30}
result=Counter(d1) +Counter(d2)
print(result)


re={key:d1.get(key , 0) + d2.get(key , 0) for key in set(d1)  |set(d2)}
print(re)
d={"a":20,"b":30}
d.update(c=20 , e="50")
print(d)
d.pop('c')
print(d)
value=[]
for i , j in d.items():
    value.append([i , j])
print(value)