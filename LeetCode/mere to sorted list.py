class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Compare the values of the head nodes
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Create linked list nodes for list1 and list2
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Create an instance of the Solution class
obj = Solution()

# Merge list1 and list2
result = obj.mergeTwoLists(list1, list2)

# Print the merged linked list
while result:
    print(result.val, end=" ")
    result = result.next
