arr= [1,2,1,3,2,4,5,3]

seen = set()
word =[]

for i in range(len(arr)):
    if arr[i] in seen:
        word.append(arr[i])
    else:
        seen.add(arr[i])

print(seen)
print(word)



l = [('nitin' , 45) , ("rahul" , 33) , ("Nishant"  , 99)]
def test(*args):
    total = 0
    for name , age in l:
        total = total + age
    return total/len(l)

average_age=test(l)
print(average_age)
my_list=[]
for name , age in l:
    if age > average_age:
        my_list.append((name, age))
print(my_list)

p = sorted(l ,key=lambda x:x[1],reverse=True)
print(p)


def fre(arr):
    cleaned_ar=''.join(i for i in arr if i.isalnum())

    freq={}
    for i in cleaned_ar:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

arr= "good morning"
f=fre(arr)
print(f)