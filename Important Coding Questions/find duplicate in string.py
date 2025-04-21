string='my name is nitin i am trying to become a good coder'
list1={}
duplicate=[]

for i in string:
    if i in list1:
        list1[i]+=1
    else:
        list1[i]=1
print(list1,duplicate)

for word, count in list1.items():
    if count >1:
        duplicate.append(word)
print(''.join(f"duplicate words are:,{duplicate}"))


print("valid string id:",list1)
print("duplicate string id:",duplicate)

string = 'my name is nitin i am trying to become a good coder'
unique_characters = []
duplicate_characters = []

for char in string:
    if char in unique_characters:
        if char not in duplicate_characters:
            duplicate_characters.append(char)
    else:
        unique_characters.append(char)

print("Unique characters:","".join(unique_characters) )
print("Duplicate characters:","".join(duplicate_characters))


keys =[1 ,2 ,3,4 ]
value=['n' , 'w' , 'r' , 't' , 'y']
result=dict(zip(keys,value))
print(result)
