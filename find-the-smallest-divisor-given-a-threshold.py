class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low, high = 1, max(nums)
        def meetThres(divisor):
            ans = 0
            for n in nums:
                ans += n//divisor
                if n%divisor > 0:
                    ans += 1
            return ans <= threshold
        while low + 1 < high:
            mid = (low + high)/2
            if meetThres(mid):
                high = mid
            else:
                low = mid
        if meetThres(low):
            return low
        else:
            return high
