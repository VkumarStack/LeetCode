# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        memo = {}
        minimum = [None, None]
        self.search(root, p, memo, minimum)
        self.search(root, q, memo, minimum)
        return minimum[0]

    def search(self, root, node, memo, minimum, depth=0):
        if root is None:
            return
        
        if root.val in memo:
            memo[root.val][0] = memo[root.val][0] + 1
            if memo[root.val][0] == 2:
                if minimum[0] is None:
                    minimum[0] = root
                    minimum[1] = depth
                else:
                    if depth > minimum[1]:
                        minimum[0] = root
                        minimum[1] = depth
        else:
            memo[root.val] = [1, depth]
        
        if root.val == node.val:
            return
        if root.val > node.val:
            self.search(root.left, node, memo, minimum, depth + 1)
        if root.val < node.val:
            self.search(root.right, node, memo, minimum, depth + 1)