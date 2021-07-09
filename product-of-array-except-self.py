class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_idx = []
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zeros_idx.append(i)
            else:
                product *= n
        res = [0]*len(nums)
        if len(zeros_idx) == 1:
            for i in zeros_idx:
                res[i] = product if len(zeros_idx) < len(nums) else 0
        elif len(zeros_idx) == 0:
            for i in range(len(nums)):
                res[i] = product//nums[i]

        return res
                
