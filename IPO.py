"""
finish at most k distinct projects
maximize the total capital
profits[i] - pure profit
capital[i] - minimum capital needed to start
w - initial capital

k=2, w=0, profits [1 2 3], capital [0 1 1]

use heap? greedy approach?

"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort(key = lambda x: -x[0])
        count = 0
        available = []
        while k > 0:
            while projects and projects[-1][0] <= w:
                heappush(available, -projects.pop()[1])
            if available:
                w += (-heappop(available))
            else:
                break
            k -= 1
            
        return w
        
