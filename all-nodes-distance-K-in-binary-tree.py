# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            elif node == target:
                subtreeAdd(node, 0) # add nodes K-0 distance
                return 1
            else:
                L = dfs(node.left)
                R = dfs(node.right)
                if L != -1: # target is in left subtree
                    if L == K:
                        ans.append(node.val)
                    subtreeAdd(node.right, L+1)
                    return L+1
                elif R != -1:
                    if R == K:
                        ans.append(node.val)
                    subtreeAdd(node.left, R+1)
                    return R+1
                else:
                    return -1
        def subtreeAdd(node: TreeNode, dis: int) -> None:
            if not node:
                return
            elif dis == K:
                ans.append(node.val)
            else:
                subtreeAdd(node.left, dis+1)
                subtreeAdd(node.right, dis+1)
        dfs(root)
        return ans
