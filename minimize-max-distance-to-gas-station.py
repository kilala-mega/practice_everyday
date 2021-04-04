class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        # stations in strictly increasing order
        # penalty is max(stations[i+1] - stations[i]) i = 0...len(stations)-2
        # add k new stations
        # return smallest possible value of penalty
        if not stations:
            return 0
        N = len(stations)
        def possible(d):
            # whether with <= k extra stations, the penalty is d
            return sum(int((stations[i+1] - stations[i]) / d)
                       for i in xrange(len(stations) - 1)) <= k
        low, high = 1e-6, stations[N-1]-stations[0]
        while low + 1e-6< high:
            mid = (low+high)/2.0
            if possible(mid):
                high = mid
            else:
                low = mid
        if possible(low):
            return low
        elif possible(high):
            return high
        else:
            return 0
        
