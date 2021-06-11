"""
k server 0 .. k-1
each server can handle at most one request at a time
each server has infinite computational capacity
round robin + fail over to next server. If full load, drop request
arrival is *strictly* increasing - arrival time of i-th request
load[i] - time to complete i-th request
busiest server(s)

"""
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requests_handled = [0]*k
        after = [] # servers at i%k and later
        before = list(range(k)) # servers wrapping around
        busy = [] # servers running requests (end time, node)
        
        for i, (arrival_time, duration) in enumerate(zip(arrival, load)):
            node = i%k
            if node == 0:
                after = before
                before = []
                
            while busy and busy[0][0] <= arrival_time:
                available_node = heappop(busy)
                if available_node[1] >= node:
                    heappush(after, available_node[1])
                else:
                    heappush(before, available_node[1])
            
            candidates = after if after else before
            if not candidates:
                continue
            using_node = heappop(candidates)
            requests_handled[using_node] += 1
            heappush(busy, (arrival_time+duration, using_node))
        
        maxrequests = max(requests_handled)
        return [i for i, totalrequests in enumerate(requests_handled) if totalrequests == maxrequests]
        
        
