class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = 0
        res = 0
        presum_map = {0:[-1]}
        for i, num in enumerate(nums):
            presum += num
            if presum-goal in presum_map:
                res += len(presum_map[presum-goal])
            if presum in presum_map:
                presum_map[presum].append(i)
            else:
                presum_map[presum] = [i]
        
        return res
            
        
