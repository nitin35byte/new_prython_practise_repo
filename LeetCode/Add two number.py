# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode()
        current = dummy_head
        carry = 0  # This will hold the carry from addition

        # Traverse both linked lists simultaneously
        while l1 or l2 or carry:
            # Get values from current nodes or default to 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            sum_val %= 10

            # Create a new node with the sum value
            current.next = ListNode(sum_val)
            current = current.next

            # Move to the next nodes in both lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next

# Example usage:
# Construct linked list l1: 2 -> 3 -> 4
l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

# Construct linked list l2: 3 -> 5 -> 6
l2 = ListNode(3)
l2.next = ListNode(5)
l2.next.next = ListNode(6)

# Create a Solution instance
solution = Solution()

# Call addTwoNumbers method with the ListNode objects l1 and l2
result = solution.addTwoNumbers(l1, l2)

# Print the result linked list (representing the sum of 234 + 356 = 590)
while result:
    print(result.val, end=" -> ")
    result = result.next
# Output: 0 -> 9 -> 5 (representing 590)



