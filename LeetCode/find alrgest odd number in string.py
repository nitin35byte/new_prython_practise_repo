

def find_largest_odd_number(s):
    max_odd=None

    for char in s:
        if char.isdigit():
            nume = int(char)
            if nume %2==1:
                if max_odd is None or nume >max_odd:
                    max_odd= nume

    return max_odd

input_string = "37"
largest_odd = find_largest_odd_number(input_string)

if largest_odd is not None:
    print(f"The largest odd number in the string is: {largest_odd}")
else:
    print("No odd numbers found in the string.")


## Leet code solution

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = -1

        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                res = i
        if res == -1:
            return ""
        else:
            return str(num[0:res + 1])
