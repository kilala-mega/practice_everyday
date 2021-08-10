class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals, reverse=True)
        res = {} # map result to q
        heap = []
        
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                # interval start <= q
                start, end = intervals.pop()
                heappush(heap, (end-start+1, end))
            while heap and heap[0][1] < q:
                heappop(heap)
            res[q] = heap[0][0] if heap else -1
            
        return [res[q] for q in queries]
