class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Your code here
        count = 0
        fre = {}
        for num in arr:
            complement = target - num
            if complement in fre:
                count += fre[complement]
            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1

        return count


def two_sum2(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left + 1, right + 1)  # Return 1-based indices (as in typical Two Sum II problem)
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase the sum
        else:
            right -= 1  # Move right pointer to the left to decrease the sum

    return None  # No solution found


# Example usage:
arr = [2, 7, 11, 15]
target = 9
result = two_sum2(arr, target)
if result:
    print("Indices of the two numbers:", result)
else:
    print("No solution found.")





