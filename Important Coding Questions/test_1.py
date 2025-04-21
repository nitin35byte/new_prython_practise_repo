class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the shortest string in the list
        shortest_str = min(strs, key=len)

        # Initialize the longest common prefix as empty
        longest_common_prefix = ""

        # Check each character index of the shortest string
        for i in range(len(shortest_str)):
            current_char = shortest_str[i]

            # Compare this character with the same index character of all strings
            for string in strs:
                if string[i] != current_char:
                    return longest_common_prefix

            # If current character matches all strings at this index, add to prefix
            longest_common_prefix += current_char

        return longest_common_prefix


# Example usage
obj = Solution()
strs = ["nitin", "nitish", "nishant", "nitesh"]
# strs = ["flower", "flow", "flight"]
print(obj.longestCommonPrefix(strs))  # Expected output: ""
