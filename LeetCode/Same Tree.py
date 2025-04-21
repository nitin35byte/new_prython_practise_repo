# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # If both nodes are None, trees are the same
        if not p and not q:
            return True

        # If one node is None and the other is not, trees are not the same
        if not p or not q:
            return False

        # If the values of the nodes are different, trees are not the same
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Helper function to create a binary tree from a list
def create_tree_from_list(vals):
    if not vals:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Example usage
# Create first tree
vals1 = [1, 2, 3]
root1 = create_tree_from_list(vals1)

# Create second tree
vals2 = [1, 2, 3]
root2 = create_tree_from_list(vals2)

# Create an instance of Solution and check if the trees are the same
sol = Solution()
print(sol.isSameTree(root1, root2))  # Output: True

# Modify second tree
vals3 = [1, 2, 4]
root3 = create_tree_from_list(vals3)
print(sol.isSameTree(root1, root3))  # Output: False
