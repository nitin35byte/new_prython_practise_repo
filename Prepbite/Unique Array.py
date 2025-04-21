def max_unique_array_length(N, arr):
    # Initialize a set to store visited indices
    visited = set()
    max_length = 0

    # Iterate through each index in the array
    for i in range(N):
        length = 0
        curr_index = i

        # Continue until we encounter a duplicate element or reach the end of the array
        while curr_index not in visited:
            visited.add(curr_index)
            length += 1
            curr_index = arr[curr_index]

        # Update the maximum length
        max_length = max(max_length, length)

    return max_length

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the size of the array and the array elements
    N = int(input())
    arr = list(map(int, input().split()))

    # Find the maximum length of the unique array
    max_length = max_unique_array_length(N, arr)

    # Print the result
    print(max_length)
