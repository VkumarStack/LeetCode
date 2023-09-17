# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        if (root.left is not None):
            self.invertTree(root.left)
        if (root.right is not None):
            self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root