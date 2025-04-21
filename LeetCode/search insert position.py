class Solution(object):
    def searchInsert(self, nums, target):

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)

obj = Solution()

nums= [2,3,4,2]
tagret = 5

result = obj.searchInsert(nums , tagret)
print(result)