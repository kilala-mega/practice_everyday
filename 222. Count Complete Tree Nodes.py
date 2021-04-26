# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node: TreeNode) -> int:
        '''
        Return tree depth in O(depth) time.
        '''
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return 1 + (2**leftDepth - 1) + self.countNodes(root.right)
        else:
            return 1 + (2**rightDepth - 1) + self.countNodes(root.left)
