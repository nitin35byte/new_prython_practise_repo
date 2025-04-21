def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b

f1 = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

def fibb(num):
    a, b = 0, 1
    for _ in range(num):
        a , b=b ,a+b
        yield a
num = 10
fib=fibb(num)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
s = 'ddfjdfhdhfdkjfhfhffg'
ch = {}
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i] = 1

max_char=max(ch,key=ch.get)
print(max_char)
print(len(ch))
def u(num):
    a,b=0,1
    for _ in range(num):
        a, b=b,a+b
        yield a
num=20
f=u(num)
print(next(f))


def max_min(num):
    maximum = num[0]
    minimum = num[0]

    for i in num:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum, minimum

l = [20, 30, 40, 50, 60, 33]
max_val, min_val = max_min(l)
print("Maximum:", max_val)
print("Minimum:", min_val)

s = 'ddfjdfhdhfdkjfhfhffg'
l1= ''

for i in s:
    if i in l1:
        l1[i] =+1
    else:
        l1=1

print(l1)


def start_end(arr , target):
    starting_point = -1
    end_point = -1

    for i in range(len(arr)):
        if arr[i] == start:
            if starting_point == -1:
                starting_point = i
            end_point = i

    return starting_point , end_point

arr =[11 , 23,44 ,56, 1 ,23, 4 ]
target = 10
start , end = start_end(arr ,target )
if target ==-1:
    print("lement not found")
else:
    print("starting point:", start)
    print("Ending point:" , end )


