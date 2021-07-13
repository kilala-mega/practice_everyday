class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presums_count = Counter()
        presums_count[0] += 1
        ans = 0
        presum = 0
        for num in nums:
            presum += num
            if presum - k in presums_count:
                ans += presums_count[presum-k]
            presums_count[presum] += 1
        return ans
