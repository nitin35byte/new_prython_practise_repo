class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Initialize carry as 1 to add 1 to the least significant digit
        carry = 1
        n = len(digits)

        # Traverse the digits array from right to left
        for i in range(n - 1, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10  # Update current digit
            carry = sum // 10  # Update carry

            # If carry becomes 0, no need to continue
            if carry == 0:
                break

        # If carry is still 1 after the loop, we need to add a new digit (1) at the beginning
        if carry == 1:
            digits.insert(0, 1)

        return digits


# Example usage:
solution = Solution()
digits = [1, 2, 3]
result = solution.plusOne(digits)
print("Result after adding one:", result)
