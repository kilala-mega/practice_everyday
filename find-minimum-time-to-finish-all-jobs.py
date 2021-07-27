"""
integer jobs
i th job
k workers 
each job -> exactly one worker
min (max working time for any worker)
"""
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        worker = [0] * k
        self.res = float('inf')
        self.start = 0
        def dfs(pos: int) -> None:
            self.start += 1
            if pos == len(jobs):
                self.res = min(self.res, max(worker))
                return
            seen = set()
            for index in range(self.start, self.start+k):
                i = index % k
                if worker[i] in seen:
                    continue
                if worker[i] > self.res:
                    continue
                seen.add(worker[i])
                worker[i] += jobs[pos]
                dfs(pos+1)
                worker[i] -= jobs[pos]
            
        dfs(0)
        return self.res
        
