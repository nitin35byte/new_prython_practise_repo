def rearrange_array(arr):
    # Sort the array to get maximum and minimum elements
    arr.sort()

    # Initialize pointers for the leftmost and rightmost elements
    left, right = 0, len(arr) - 1

    # Initialize an empty result list to store rearranged elements
    result = []

    # Iterate over the array, alternately appending maximum and minimum elements
    while left <= right:
        # Append the maximum element from the right side
        result.append(arr[right])

        # If there are more than one element remaining, append the minimum element from the left side
        if left != right:
            result.append(arr[left])

        # Move pointers towards the middle
        left += 1
        right -= 1

    return result


# Example usage:
arr = [1, 2, 3, 4, 5]
print(rearrange_array(arr))  # Output: [5, 1, 4, 2, 3]



### Prepbite

def rearrange_array(arr):
    # Sort the array
    arr.sort()

    # Initialize the result array
    result = []

    # Pointers to keep track of maximum and minimum elements
    left, right = 0, len(arr) - 1

    # Traverse the array and rearrange elements
    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1

    return result

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the size of the array
    N = int(input())

    # Input the array elements
    arr = list(map(int, input().split()))

    # Rearrange the array according to the specified pattern
    rearranged_arr = rearrange_array(arr)

    # Print the rearranged array
    print(*rearranged_arr)
