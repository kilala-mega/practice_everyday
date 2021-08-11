class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [[0]*n for i in range(2)]
        
        dp[0][0] = nums[0] # no square
        dp[1][0] = nums[0]**2 # square
        
        res = dp[1][0]
        
        for i in range(1, len(nums)):
            dp[0][i] = max(nums[i], nums[i]+dp[0][i-1])
            dp[1][i] = max(nums[i]**2, nums[i]**2+dp[0][i-1], nums[i]+dp[1][i-1])
            res = max(res, dp[0][i], dp[1][i])
        
        return res
