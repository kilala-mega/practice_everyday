"""
maximum subarray of (total - x)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if not nums:
            return - 1
        target = sum(nums)-x
        h = {0:-1}
        presum = 0
        ans = 0
        if target == 0:
            return len(nums)
        last = -1
        for i,num in enumerate(nums):
            presum += num
            if presum-target in h:
                if i-h[presum-target] > ans:
                    ans = i-h[presum-target]
                    last = i
            if presum not in h:
                h[presum] = i
        res = len(nums)-ans if ans > 0 else -1
        
        return res
