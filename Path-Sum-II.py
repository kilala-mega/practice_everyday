# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        pathLists = []
        self.recurseTree(root, [], pathLists, targetSum)
        return pathLists
    
    def recurseTree(self, node: TreeNode, pathVals: List[int], pathLists: List[List[int]], remainSum: int) -> None:
        if not node:
            return
        pathVals.append(node.val)
        remainSum -= node.val
        if remainSum == 0 and not node.left and not node.right:
            # find a path pathVals, add it to the final results
            pathLists.append(pathVals[:])
        else:
            self.recurseTree(node.left, pathVals, pathLists, remainSum)
            self.recurseTree(node.right, pathVals, pathLists, remainSum)
        pathVals.pop()
