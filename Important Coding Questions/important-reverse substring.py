def reverse_substrings_before_numbers(s):
    index = 0
    result=""

    while index  <len(s):

        if s[index].isdigit():
            index +=1

            continue

        substring=""

        while index <len(s) and not s[index].isdigit():

            substring +=s[index]
            index +=1

        result+=substring[::-1]

    return result
    return result

s = "fdsaf4sagtt6hrdhhj7gh9"
result = reverse_substrings_before_numbers(s)
print(result)  # Output: "asdfttgasjhhdrhhg"



def reverser_substrib(a):
    index = 0
    result =""

    while index <len(a):

        if a[index].isalpha():
            index+=1

            continue

        substring1=""

        while index<len(a) and not a[index].isalpha():
            substring1+=a[index]

            index +=1

        result+=substring1[::-1]

    return  result

a = "fdsaf4sagtt6hrdhhj7gh9"
result = reverser_substrib(a)
print(result)  # Output: "asdfttgasjhhdrhhg"

fre={}
for i in a:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(f"char frequency is {fre}")

l=''.join(f'{char} , {count}' for char , count in fre.items())
print(l)

result=''
for char , count in fre.items():
    result+=f"{char}{count}"
print(f"resullts are{result}")