"""
sort the events by startDay and endDay
use a heap
from day 1 to max(endDay), see if there is a new event to attend
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res = 0
        h = []
        heapify(h)
        for d in range(1, 100001):       
            while events and events[0][0] <= d:
                heappush(h, events.pop(0)[1])
            while h and h[0] < d:
                heappop(h)                
            if h:
                res += 1
                heappop(h)
            if not events and not h:
                break
        
        return res
        
