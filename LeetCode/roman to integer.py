class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_val = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                int_val -= val[s[i]]
            elif i + 1 < len(s) and s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                int_val -= val[s[i]]
            elif i + 1 < len(s) and s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                int_val -= val[s[i]]
            else:
                int_val += val[s[i]]
        return int_val
