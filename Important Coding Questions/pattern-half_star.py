row=int(input("enter number of rows:"))

for i in range(row):
    for j in range(1 , i+1):
        print("*" , end='')
    print()


rows=int(input("enter number of rows:"))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(i-1 , 0 , -1):
        print(k , end ='')
    print()

def max_profit(arr):
    n= len(arr)
    profit=0
    for i in range(n):
        if arr[i] >arr[i-1]:
            profit+=arr[i]-arr[i-1]

    return profit

arr=[2,5,3,6,9]
print(max_profit(arr))

