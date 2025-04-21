class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize two pointers: one for iterating through the list (`i`)
        # and another for keeping track of the position to insert non-`val` elements (`j`)
        i = 0
        j = 0

        # Iterate through the list using the `i` pointer
        while i < len(nums):
            # If the current element is not equal to `val`, keep it in the list
            if nums[i] != val:
                # Move the element to the position pointed by `j`
                nums[j] = nums[i]
                # Increment `j` to point to the next position
                j += 1
            # Move `i` to the next element in the list
            i += 1

        # `j` now represents the length of the modified list with `val` removed
        return j

# Create an instance of the Solution class
obj = Solution()

# Input list and value to remove
nums = [3, 2, 2, 3, 4, 2, 5]
val = 2

# Call the removeElement method to remove all occurrences of `val` from `nums`
new_length = obj.removeElement(nums, val)

# Print the modified list and its new length
print("Modified List:", nums[:new_length])
print("New Length:", new_length)
