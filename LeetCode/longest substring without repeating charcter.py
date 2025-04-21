class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        max_length = 0
        start = 0

        # Traverse the string with two pointers: start and end
        for end in range(len(s)):
            # Check if the current character is already in the dictionary
            if s[end] in char_index:
                # Update the start pointer to the next position after the last occurrence of s[end]
                start = max(start, char_index[s[end]] + 1)

            # Update the most recent index of the current character
            char_index[s[end]] = end

            # Calculate the length of the current substring without repeating characters
            max_length = max(max_length, end - start + 1)

        return max_length


# Test the Solution class







solution = Solution()
input_str = "abcabcbb"
result = solution.lengthOfLongestSubstring(input_str)
print("Length of the longest substring without repeating characters:", result)



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        max_length = 0
        start = 0

        # Traverse the string with an end pointer
        for end in range(len(s)):
            # If the character is already in the set, slide the start pointer
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1

            # Add the current character to the set
            char_set.add(s[end])

            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length

