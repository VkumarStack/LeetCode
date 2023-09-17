# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        result = []
        result.append(root.val)
        self.maxPathRecur(root, result)
        return result[0]

    def maxPathRecur(self, root, globalMax):
        if root is None:
            return 0
        leftMax = self.maxPathRecur(root.left, globalMax)
        rightMax = self.maxPathRecur(root.right, globalMax)
        leftRightSum = root.val
        if (leftMax + root.val) >= root.val:
            leftRightSum += leftMax
        if (rightMax + root.val) >= root.val:
            leftRightSum += rightMax
        globalMax[0] = max(globalMax[0], leftRightSum, root.val + leftMax, root.val + rightMax)
        if (leftMax + root.val) >= root.val and (leftMax >= rightMax):
            return leftMax + root.val
        elif (rightMax + root.val) >= root.val and (rightMax > leftMax):
            return rightMax + root.val
        return root.val

root = TreeNode(1, TreeNode(2), TreeNode(3))
soln = Solution()
print(soln.maxPathSum(root))