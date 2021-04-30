# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def edgeLength(node: TreeNode) -> int:
            if not node:
                return 0
            leftLength, rightLength = edgeLength(node.left), edgeLength(node.right)
            leftEdge, rightEdge = 0, 0
            if node.left and node.left.val == node.val:
                leftEdge = leftLength + 1
            if node.right and node.right.val == node.val:
                rightEdge = rightLength + 1
            self.ans = max(self.ans, leftEdge + rightEdge)
            return max(leftEdge, rightEdge)
        edgeLength(root)
        return self.ans
