from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        ret = ""
        if root is None:
            return ret
        ret = str(root.val) + ","
        que = deque()
        que.append(root)
        while len(que) != 0:
            node = que.popleft()
            if node.left is not None:
                ret = ret + str(node.left.val) + ","
                que.append(node.left)
            else:
                ret = ret + str("null,")

            if node.right is not None:
                ret = ret + str(node.right.val) + ","
                que.append(node.right)
            else:
                ret = ret + str("null,")
        return ret


    def deserialize(self, data):
        ret = data.split(',')
        i = len(ret) - 1
        endNull = True
        while i >= 0:
            if (ret[i] == 'null' or ret[i] == '') and endNull:
                del ret[i]
            elif ret[i] != 'null':
                endNull = False
                ret[i] = int(ret[i])
            else:
                ret[i] = None
            i = i - 1
        return ret

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
test = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(test.deserialize(test.serialize(root)))