def first_middle_last(string):
    length = len(string)
    if length<=1:
        return string

    middle = string[length // 2] if length % 2 != 0 else string[length // 2 - 1]
    print(middle)
    result =string[0] + middle + string[-1]
    return  result

string = 'nitineee'
print(first_middle_last(string))


a = 'nitin'

for i in a:
    if i == 't':
        continue
print(a)


lower =1
upper = 10

for i in range(lower , upper +1):
    for j in range(2 , i):
        if i %j ==0:
            break
    else:

        print(i)