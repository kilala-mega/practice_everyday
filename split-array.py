class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums:
            return 0
        # largest sum among m subarrays
        # dfs with memorized result
        # dp[i][j] the largest sum of splitting nums[0..i] into j parts 
        # i=0...n (n=len(nums))
        # j = 0...m
        # dp[0][0] = 0 
        # dp[i][j] = min(dp[k][j-1], sum(nums[k:i])) k in 0 ... i-1
        # ans dp[n][m]
        n = len(nums)
        dp = [[float('inf')] * (m+1) for i in range(n+1)]
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(0, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], presum[i] - presum[k]))
        return dp[n][m]
         
