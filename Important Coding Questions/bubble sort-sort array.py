def bubblesort(s):
    n = len(s)
    for i in range(n):
        for j in range(0 , n-i-1):
            if s[j] >s[j+1]:
                s[j] , s[j+1]=s[j+1] , s[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubblesort(arr)
print("Sorted array t:", arr)



def Test(s):
    n = len(s)
    for i in range(n):
        for j in range(0 , n-i-1):
            if s[j] >s[j+1]:
                s[j] , s[j+1]=s[j+1] , s[j]

arr = [64, 34, 25, 12, 22, 11, 90]
Test(arr)
print("Sorted array:", arr)


n =sorted(arr)
print(n)

arr = [64, 34, 25, 12, 22, 11, 90]
c= sorted(arr)
print("sorted data :",c)