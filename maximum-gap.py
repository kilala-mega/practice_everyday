'''
requirement linear time and linear space
3 9 6 1
[3, 9] 
diff_so_far = 6 
find the maximum diff
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        exp = 1
        maxVal = max(nums)
        aux = [0] * len(nums)
        while maxVal//exp > 0:
            count = [0] * 10
            for i in range(len(nums)):
                count[(nums[i]//exp)%10] += 1
            
            for i in range(1,len(count)):
                count[i] += count[i-1]
                
            for i in range(len(nums)-1,-1,-1):
                aux[count[(nums[i]//exp)%10] - 1] = nums[i]
                count[(nums[i]//exp)%10] -= 1
            
            for i in range(len(nums)):
                nums[i] = aux[i]
            
            exp *= 10
        
        maxGap = 0
        for i in range(1, len(nums)):
            maxGap = max(maxGap, nums[i]-nums[i-1])
        return maxGap
