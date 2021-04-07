# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        positions = {}
        for i, val in enumerate(inorder):
            positions[val] = i
        self.index = len(postorder)
        def helper(start, end):
            if start > end:
                return None
            self.index -= 1
            if self.index < 0:
                return None
            val = postorder[self.index]
            pos = positions[val]
            root = TreeNode(val)
            root.right = helper(pos+1,end)
            root.left = helper(start,pos-1)
            return root
        return helper(0, len(inorder)-1)
