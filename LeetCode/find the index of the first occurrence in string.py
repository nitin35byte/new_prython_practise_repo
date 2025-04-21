class Solution(object):
    def strStr(self, haystack, needle):

        index = haystack.find(needle)
        if index != -1:
            print("index is:", index)
            return index
        else:
            print("index not found")
            return -1


solution = Solution()
haystack = "hello world"
needle = "lo"
result = solution.strStr(haystack, needle)
print("Index of substring:", result)


