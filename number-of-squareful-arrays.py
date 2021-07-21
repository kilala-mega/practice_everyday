"""
array of nums
>0
integer
squareful

"""
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.ans = 0
        nums.sort()
        def dfs(nums, curr):
            if not nums:
                self.ans += 1
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if not curr or int(sqrt(nums[i]+curr[-1])) == sqrt(nums[i]+curr[-1]):
                    curr.append(nums[i])
                    dfs(nums[:i]+nums[i+1:], curr)
                    curr.pop()
                
        dfs(nums, [])
        return self.ans
        
        
