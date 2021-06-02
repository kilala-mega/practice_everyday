class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        start, end = 0, maxSum
        while start + 1 < end:
            mid = (start + end)//2
            if self.getSum(mid, index, n) <= maxSum:
                start = mid
            else:
                end = mid
        if self.getSum(end, index, n) <= maxSum:
            return end+1
        elif self.getSum(start, index, n) <= maxSum:
            return start+1
        else:
            return -1
    
    def getSum(self, target: int, index: int, n: int) -> int:
        ans = 0
        leftmost = max(0, target-index)
        ans += (target+leftmost)*(target-leftmost+1)/2
        rightmost = max(0, target-(n-1-index))
        ans += (rightmost+target)*(target-rightmost+1)/2
        return ans - target
