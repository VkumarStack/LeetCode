class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        starts = []
        self.search(root, subRoot, starts)
        if len(starts) == 0:
            return False
        for start in starts:
            if self.checkSubtree(start, subRoot):
                return True
        return False
        
    def search(self, root, subRoot, starts):
        if root is None:
            return
        if root.val == subRoot.val:
            starts.append(root)
        self.search(root.left, subRoot, starts)
        self.search(root.right, subRoot, starts)
    
    def checkSubtree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return (self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right))