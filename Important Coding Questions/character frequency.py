def char_frequency(str1):

    dict = {}

    for n in str1:
        keys = dict.keys()

        if n in keys:
           dict[n] +=1

        else:
           dict[n] =1

    return dict

        # Call the char_frequency function with the argument 'google.com' and print the result.
#print(char_frequency('google.com')
## Without function


words = input("Enter your string:")

dict = {}

for n in words:
    keys = dict.keys()

    if n in keys:
        dict[n] +=1

    else:
        dict[n] =1

print(dict)

        # Call the char_frequency function with the argument 'google.com' and print the result.
#print(char_frequency('google.com'))

n = "Niitn"
d={}
for i in n:
    if i in d:
        d[i] +=1
    else:
        d[i]=1

print("frequency id :",d)


a = "infosys private limited"
b={}

d =[]

for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i] =1
print(b)

for value, count in b.items():
    if count >1:
        d.append(value)
print(d)


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





d = {'name':"nitin",
     'age':29,
     "location":"delhi"
}

d.pop('location')
print(d)


def fibb():
    a , b=0 ,1
    while True:
        yield a
        a ,b=b ,a+b

f=fibb()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))



a=(2,)
print(type(a))