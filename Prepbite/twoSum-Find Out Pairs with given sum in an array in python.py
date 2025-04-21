def twosum(arr , target):
    left =0
    right=len(arr)-1

    while(left <= right):
        if arr[left]+arr[right] >target:
            right=right-1
        elif arr[left]+arr[right]<target:
            left = left +1

        else:
            print(f'Values of {arr[left]} & {arr[right]} is {target}')

            left = left + 1
            right = right - 1
target = 17
arr = [5, 7, 4, 3, 9, 8, 19, 21]
twosum(arr, target)


arr = [5, 7, 4, 3, 9, 8, 19, 21]
lts = 11

for i in range(len(arr)):
    for j in range(i):  # Iterate only through previous elements
        if arr[i] + arr[j] == lts:
            print(f"{arr[i]} , {arr[j]} -> {arr[i] + arr[j]}")


arr = [5, 7, 4, 3, 9, 8, 19, 21]
mazimun=0
secon_maximmum=0
lowest=arr[0]
for i in range(len(arr)):
    if arr[i] > mazimun:
        secon_maximmum=mazimun
        mazimun=arr[i]

    elif arr[i]>secon_maximmum:
        secon_maximmum=arr[i]
    elif arr[i] <lowest:
        lowest=arr[i]


print(mazimun ,secon_maximmum ,lowest)