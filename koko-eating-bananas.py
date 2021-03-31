class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # min speed k to finish all the bananas in h hours
        if not piles:
            return -1
        n = len(piles)
        if n > h:
            return -1
        def possible(K):
            countHours = 0  # hours take to eat all bananas
            for pile in piles:
                countHours += pile / K
                if pile % K != 0:
                    countHours += 1
            return countHours <= h
        
        low, high = 1, max(piles)
        while low + 1 < high:
            mid = (low + high)/2
            if not possible(mid):
                low = mid # eat too slow
            else:
                high = mid
        if possible(low):
            return low
        else:
            return high
