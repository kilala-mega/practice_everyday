# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # find middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        
        # reverse the latter half
        prev, curr = None, middle
        while curr:
            later = curr.next
            curr.next = prev
            prev = curr
            curr = later
            
        new_middle = prev
        # merge two lists
        curr = head
        dummy = ListNode()
        newhead = dummy
        while curr is not None and new_middle is not None:
            dummy.next = curr
            dummy = dummy.next
            curr = curr.next
            
            dummy.next = new_middle
            new_middle = new_middle.next
            dummy = dummy.next
        
        while curr:
            dummy.next = curr
            curr = curr.next
            dummy = dummy.next
            
        return newhead.next
