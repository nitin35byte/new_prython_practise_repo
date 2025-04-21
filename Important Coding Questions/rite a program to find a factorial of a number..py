num = int(input("enter number"))

factorial = int(input("enter factorial"))

if num < 0:
    print("factorial of 0 is one")

elif num ==1:
    print("factorla of 1 is 1")

else:
    for i in range(1 , num+1):
        factorial = factorial*i

    print("The factorial of", num, "is", factorial)




num1 = input("enter number")

if num <0:
    print("sbsn")


elif  num ==1:
    print("1")
else:
    factorial1 =1
    for i in range(i , num+1):
        factorial1 = factorial1 *i
    print("The factorial of", num1, "is", factorial)




def fact(num):
    if num <0:
        print(f"factorail of {num} is 1")
    elif num ==1:
        print(f"factorail of {num} is 1")
    else:
        factorial =1
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num1, "is", factorial)



def palindrome(name):
    name = name.lower()
    left = 0
    right = len(name)-1

    while left <right:
        if name[left] != name[right]:
            print(f"{name}, is Not a palindrome")
            return  False
        left +=1
        right -=1
    print("Plaindrome")
    return True
a = "rahul"
b =palindrome(a)
print(b)


employee= [("nitin" , 10000),('rahul' , 2300),('sumit',30000)]

total = 0
for name, salary in employee:
    total_salary= total +salary

    print(total)

c=["nitin" , "nitish","rahul" ,"kumal"]
r=[i for i in c if i.startswith("n")]
print(r)

for i in c:
    if i[0]=="r":
        print(i)