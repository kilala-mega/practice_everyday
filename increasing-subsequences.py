class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(nums, curr):
            if len(curr) >= 2:
                res.add(tuple(curr))
            for i in range(len(nums)):
                if not curr or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                    backtrack(nums[i+1:], curr)
                    curr.pop()
        backtrack(nums, [])
        return list(res)
        
