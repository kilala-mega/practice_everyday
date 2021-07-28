"""
[[1,2],[3,6],[1,3],[10,1]]
"""
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        t = tasks[0][0]
        point = 0
        h = []
        ans = []
        while point < len(tasks) or h:
            while point < len(tasks) and tasks[point][0] <= t:
                heappush(h, (tasks[point][1], tasks[point][2]))
                point += 1
            if h:              
                processed = heappop(h)
                ans.append(processed[1])
                t += processed[0]
            elif point < len(tasks):
                t = tasks[point][0]
        return ans 
