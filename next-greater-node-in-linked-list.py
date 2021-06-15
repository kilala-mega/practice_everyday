# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        while head:
            while stack and head.val > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = head.val
            stack.append((head.val, len(res)))               
            res.append(0)
            head = head.next
        return res
        
