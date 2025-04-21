def find_greater_eleents(arr):
    n = len(arr)
    result = []
    max_right = float('-inf')

    for i in range(n-1 , -1 , -1):
        if arr[i]>=max_right:
            result.append(arr[i])
            max_right= arr[i]

    return result[::-1]




T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    print(find_greater_eleents(arr))