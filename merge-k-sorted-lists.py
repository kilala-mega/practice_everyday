# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        h = []
        for node in lists:
            if node:
                heappush(h, Wrapper(node))
        dummy = ListNode()
        newhead = dummy
        while h:
            node = heappop(h).node
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heappush(h, Wrapper(node.next))
        
        return newhead.next
    
