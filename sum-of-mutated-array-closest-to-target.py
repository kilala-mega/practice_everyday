"""
arr: List[int]
target: int
@return int
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        start, end = 0, max(arr)
        def getSum(mid: int) -> int:
            res = 0
            for a in arr:
                if a > mid:
                    res += mid
                else:
                    res += a
            return res
        while start + 1 < end:
            mid = (start + end)//2
            if getSum(mid) > target:
                end = mid
            else:
                start = mid
        
        candstart = abs(getSum(start)-target)
        candend = abs(getSum(end)-target)
        if candstart <= candend:
            return start
        else:
            return end
        
        
