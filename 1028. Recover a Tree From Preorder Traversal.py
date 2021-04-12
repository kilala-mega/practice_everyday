# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        idx = 0
        stack = [] # the path from root to leaf
        while idx < len(S):
            level, val = 1, ""
            while idx < len(S) and S[idx] == '-':
                level += 1
                idx += 1
            while idx < len(S) and S[idx] != '-':
                val += S[idx]
                idx += 1
            while level <= len(stack):
                stack.pop()
            node = TreeNode(int(val))
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        
