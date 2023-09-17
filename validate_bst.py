# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        if root.left is None and root.right is None:
            return True
        return self.validate(root, None, None)
    
    def validate(self, root, minimum, maximum):
        if root is None:
            return True
        valid = True
        if minimum is not None:
            if root.val <= minimum:
                return False
    
        if maximum is not None:
            if root.val >= maximum:
                return False

        valid = self.validate(root.left, minimum, root.val) and self.validate(root.right, root.val, maximum)

        return valid


rightParent = TreeNode(5, TreeNode(4), TreeNode(6))
leftParent = TreeNode(1, TreeNode(0), TreeNode(2))
test = Solution().isValidBST(TreeNode(3, leftParent, rightParent))
print(test)
