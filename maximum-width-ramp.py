"""
(i,j) i < j and nums[i] <= nums[j], width is j-i
maximum width of a ramp
[9,8,1,0,1,9,4,0,4,1]

[(1,9),(4,8),(9,5)]
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stack = [] # items is (value, index)
        for i in range(len(nums)-1,-1,-1): # from right to left
            if not stack or nums[i] > stack[-1][0]: # note i < stack[-1][1]
                stack.append((nums[i], i))
            else:
                furthest_smaller_index = bisect.bisect(stack, (nums[i], i)) # note search for (nums[i], i)
                #print('i=', i,' nums[i]=', nums[i], ' found index', furthest_smaller_index)
                j = stack[furthest_smaller_index][1]
                res = max(res, j-i)
        return res
        
        
