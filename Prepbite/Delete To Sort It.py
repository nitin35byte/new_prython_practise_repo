def min_deletions_to_lexico_order(arr):
    deletions = 0
    for i in range(len(arr[0])):
        for j in range(1, len(arr)):
            if arr[j][i] < arr[j - 1][i]:
                deletions += 1
                break
    return deletions


# Input number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input number of strings and the strings themselves
    n = int(input())
    strings = input().split()

    # Calculate and print the minimum number of deletion operations
    print(min_deletions_to_lexico_order(strings))
