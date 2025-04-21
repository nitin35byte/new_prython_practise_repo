class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize candidate and count
        candidate = None
        count = 0

        # Find candidate using Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Verify candidate is the majority element
        # Count occurrences of candidate
        occurrences = sum(1 for num in nums if num == candidate)

        # Check if candidate is the majority element
        if occurrences > len(nums) // 2:
            return candidate
        else:
            raise ValueError("No majority element found")


# Example usage:
solution = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
result = solution.majorityElement(nums)
print("Majority element:", result)
