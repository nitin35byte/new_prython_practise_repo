def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Example usage (using brute force approach):
nums = [2, 7, 11, 15]
target = 9
result = two_sum_brute_force(nums, target)

if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}")
else:
    print("No two numbers add up to the target sum.")



# second method

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Return an empty list if no such pair is found


##Method 1: Using a Hash Map (Dictionary)
def two_sum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    num_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers that add up to the target
            return [num_dict[complement], i]

        # Store the current number and its index in the dictionary
        num_dict[num] = i

    # If no such pair is found, return an empty list or handle accordingly
    return []


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}")
else:
    print("No two numbers add up to the target sum.")



###

def twosum(arr , target):
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] + arr[right] >target:
            right = right -1
        elif arr[left] + arr[right] <target:
            left = left +1
        else:
            print(f'Values of {arr[left]} & {arr[right]} sum to {target}')
            right = right - 1
            left = left + 1


target = 17
arr = [5, 7, 4, 3, 9, 8, 19, 21]
twosum(arr, target)
