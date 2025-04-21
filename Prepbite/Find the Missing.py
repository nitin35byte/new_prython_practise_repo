def find_missing_number(N, arr):
    total_sum = N * (N + 1) // 2  # Sum of first N natural numbers
    arr_sum = sum(arr)  # Sum of elements in the array
    missing_number = total_sum - arr_sum  # Find the missing number
    return missing_number

arr = [1, 2, 4, 5, 6]

# Size of array (including the missing number)
N = len(arr) + 1
print(N)
# Find the missing number
missing_number = find_missing_number(N, arr)

print("The missing number is:", missing_number)


def find_missing_number(N, arr):
    sum_N = N * (N + 1) // 2
    sum_arr = sum(arr)

    missing_number = sum_N - sum_arr
    return missing_number


T = int(input())

for _ in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    missing_number = find_missing_number(N, arr)
    print(missing_number)


import calendar
yy=2024
mm=12
print(calendar.month(yy,mm))