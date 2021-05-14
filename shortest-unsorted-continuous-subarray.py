# [2,6,4,8,10,9,15]
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minVal, maxVal = float('inf'), float('-inf')
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                minVal = min(minVal, nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                maxVal = max(maxVal, nums[i])
        
        l, r = 0, 0        
        for i in range(len(nums)):
            if minVal < nums[i]:
                l = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if maxVal > nums[i]:
                r = i
                break
        
        return r - l + 1 if r > l else 0
