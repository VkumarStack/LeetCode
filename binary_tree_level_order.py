from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ret = []
        nodes = self.levelOrderHelper([root], ret)
        while len(nodes) != 0:
            nodes = self.levelOrderHelper(nodes, ret)
        return ret
    
    def levelOrderHelper(self, nodes, ret):
        queue = []
        level = []
        for node in nodes:
            if node is not None:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if len(level) != 0:
            ret.append(level)
        return queue