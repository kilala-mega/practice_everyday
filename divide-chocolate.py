class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        # cut into K+1 pieces, maximize the min sweetness among the K+1 pieces
        if not sweetness:
            return 0
        low, high = min(sweetness), sum(sweetness)/(K+1)
        def canCut(total):
            # whether we can have at least K+1 piece and the sum of sweetness of each piece >= total
            curr = 0
            piece = 0
            for i in range(len(sweetness)):
                if curr + sweetness[i] >= total:
                    curr = 0
                    piece +=1
                else:
                    curr += sweetness[i]
            return piece >= (K+1)
        while low + 1 < high:
            mid = (low+high)/2
            if canCut(mid):
                low = mid
            else:
                high = mid
        if canCut(high):
            return high
        else:
            return low
