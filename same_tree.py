# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        return self.sameRecur(p, q)
    def sameRecur(self, p, q):
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True
        if p.val == q.val:
            return True
        return self.sameRecur(p.left, q.left) and self.sameRecur(p.right, q.right)