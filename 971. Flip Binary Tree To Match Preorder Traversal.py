# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != voyage[i]:
                return [-1]
            i += 1
            if node.right and node.right.val == voyage[i]:
                if node.left:
                    res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
