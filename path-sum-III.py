# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        count = 0
        h = defaultdict(int)
        def search(node: TreeNode, currSum: int) -> None:
            nonlocal count
            if not node:
                return
            currSum += node.val
            if currSum == targetSum:
                count += 1
            count += h[currSum-targetSum]
            h[currSum] += 1
            search(node.left, currSum)
            search(node.right, currSum)
            h[currSum] -= 1
        search(root, 0)
        return count
