# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        point = head
        for i in range(k):
            if not point:
                return head
            point = point.next
        prev, curr = None, head
        for i in range(k):
            if not curr:
                return head
            later = curr.next
            curr.next = prev
            prev = curr
            curr = later
        if later:
            nexthead = self.reverseKGroup(curr, k)
            head.next = nexthead
        return prev
