class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def recurse(pos: int, cur: List[int]) -> None:
            res.append(cur[:])
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                recurse(i+1, cur)
                cur.pop()
        recurse(0, [])
        return res
        
