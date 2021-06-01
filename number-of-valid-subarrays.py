class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = len(nums)
        stack = [nums[0]]
        
        for i in range(1,len(nums)):
            while stack and nums[i] < stack[-1]:
                stack.pop()
            res += len(stack)
            stack.append(nums[i])
        
        return res
