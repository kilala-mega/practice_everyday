class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        
        if not weights:
            return -1
        
        def canShip(capacity):
            curr = 0
            days = 1
            for i in range(len(weights)):
                if weights[i] > capacity:
                    return False
                if curr + weights[i] > capacity:
                    curr = weights[i]
                    days += 1
                else:
                    curr += weights[i]
            return days <= D
            
        
        low, high = 1, sum(weights)
        while low + 1 < high:
            mid = (low + high)/2
            if canShip(mid):
                high = mid
            else:
                low = mid
        if canShip(low):
            return low
        elif canShip(high):
            return high
        else:
            return -1
        
