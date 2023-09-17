# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        # Need a globally mutable value
        index = [k]
        val = [None, False]
        self.inOrder(root, index, val)
        return val[0]
    def inOrder(self, root, k, val):
        if root is None:
            return None
        if root.left is not None:
            self.inOrder(root.left, k, val)
        k[0] = k[0] - 1
        if k[0] == 0 and val[1] == False:
            val[0] = root.val
            val[1] = True
            return
        if root.right is not None:
            self.inOrder(root.right, k, val)    