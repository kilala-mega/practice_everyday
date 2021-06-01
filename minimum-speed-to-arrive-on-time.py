"""
sum(ceil(dist[i]/speed) excluding n-1 + dist[n-1]/speed) <= hour
"""
import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if not dist or hour < len(dist)-1:
            return -1
        start, end = 1, 100*max(dist)
        while start + 1 < end:
            mid = (start + end)//2
            total_hour = 0
            for i in range(len(dist)):
                if i == len(dist)-1:
                    total_hour += dist[i]/mid
                else:
                    total_hour += math.ceil(dist[i]/mid)
            if total_hour > hour:
                # too slow
                start = mid
            else:
                end = mid
        total_hour = 0
        for i in range(len(dist)):
            if i == len(dist)-1:
                total_hour += dist[i]/start
            else:
                total_hour += math.ceil(dist[i]/start)
        if total_hour <= hour:
            return start
        total_hour = 0
        for i in range(len(dist)):
            if i == len(dist)-1:
                total_hour += dist[i]/end
            else:
                total_hour += math.ceil(dist[i]/end)
        if total_hour <= hour:
            return end
        return -1
        
        
                    
                
        
