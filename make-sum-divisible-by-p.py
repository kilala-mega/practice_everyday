class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # sum of subarray
        need = sum(nums)%p
        # shortest length of subarray, return -1 if not possible
        res = len(nums)
        # map of -> rightmost index: presum % p remaining. add index:remain with 0:-1 for easier calculation
        remaining = {0:-1}
        # initial value to store presum
        presum_remain = 0
        
        for i, num in enumerate(nums):
            # only interested in the %p remaining 
            presum_remain = (presum_remain + num) % p
            # create/update the rightmost index, need this line in front of the if condition
            remaining[presum_remain] = i
            # sum(nums) - sum(subarray) is divisible by p
            if (presum_remain - need)%p in remaining:
                # no need to + 1 in the length because the leftmost element is excluded in the subarray
                res = min(res, i-remaining[(presum_remain-need)%p])         
        # -1 if need to remove whole array
        return res if res < len(nums) else -1
