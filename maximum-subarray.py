class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = 0
        min_presum = 0
        res = max(nums)
        for num in nums:
            presum += num
            res = max(res, presum - min_presum)
            min_presum = min(min_presum, presum)
        return res
            
                
