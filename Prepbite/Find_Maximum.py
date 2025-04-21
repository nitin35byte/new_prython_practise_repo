def max_difference(arr):
    max_diff = -1
    n = len(arr)
    for i in range(n):
        for j in range(i+1 , n):
            if arr[j]>arr[i]:
                max_diff=max(max_diff,j-i)

    return max_diff

N = int(input())

arr= list(map(int,input().split()))

print(max_difference(arr))
