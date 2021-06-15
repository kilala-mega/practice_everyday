"""
5 3 6 7
9
[3]  [5 3] [3 6] [5 3 6]

sort first
min is on the left-side, max is on the right-side of the array
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        module = 10**9 + 7
        nums.sort()
        left, right = 0, len(nums)-1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right-left, module) # nums[left+1] .. nums[right] choose or not choose
                # we can even choose not to include nums[right], because nums[left] <= nums[right]
                # therefore 2*nums[left] <= target
                left += 1
        return ans % module
        
