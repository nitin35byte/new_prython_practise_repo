# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        seen = set()
        current = head
        seen.add(current.val)

        while current and current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next

        return head


# Example usage
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1 -> 4 -> 5 -> 3 -> 6
nodes = [ListNode(1), ListNode(2), ListNode(3), ListNode(2), ListNode(1), ListNode(4), ListNode(5), ListNode(3),
         ListNode(6)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

sol = Solution()
new_head = sol.deleteDuplicates(head)
print_list(new_head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None




def removeDuplicate(lst):
    seen = set()
    result = []

    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)

    return result

lst = [1,2,4,6,1,3,7,8,9,4,6]
lst.sort()
print(removeDuplicate(lst))