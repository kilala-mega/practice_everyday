class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if not bloomDay:
            return -1
        n = len(bloomDay)
        if n < m*k:
            return -1
        def check(day):
            count = nums = 0
            for d in bloomDay:
                if d <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    nums += 1
                    count = 0
            return nums >= m
                
        low, high = 1, max(bloomDay)
        # search number of days to wait to be able to make m bouquets (with k adjacent flowers) from the garden
        # low: wait 1 day
        # high: wait until the longest waiting flower blooming
        while low + 1 < high:
            mid = (low + high)/2
            if check(mid):
                high = mid
            else:
                low = mid
        if check(low):
            return low
        elif check(high):
            return high
        else:
            return -1
