class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        presum_hash = {0:-1}
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            if presum - k in presum_hash:
                ans = max(ans, i-presum_hash[presum-k])
            if presum not in presum_hash:
                presum_hash[presum] = i
        return ans
