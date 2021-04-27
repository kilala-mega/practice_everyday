# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        def isBSTtreeAndSize(node: TreeNode) -> tuple[int, bool, float, float]:
            if node is None:
                return 0, True, float('inf'), -float('inf')
            LeftCount, LeftIsBST, LeftMin, LeftMax = isBSTtreeAndSize(node.left)
            RightCount, RightIsBST, RightMin, RightMax = isBSTtreeAndSize(node.right)
            count = 0
            isBST = False
            if LeftIsBST and RightIsBST and node.val > LeftMax and node.val < RightMin:
                isBST = True
                count = LeftCount + RightCount + 1
                Min = LeftMin if node.left else node.val
                Max = RightMax if node.right else node.val
            elif LeftIsBST:
                count = LeftCount
                Min = LeftMin
                Max = LeftMax
            elif RightIsBST:
                count = RightCount
                Min = RightMin
                Max = RightMax
            else:
                count = 0
                Min = float('inf')
                Max = -float('inf')
            self.count = max(self.count, count)
            return count, isBST, Min, Max
        isBSTtreeAndSize(root)
        return self.count
