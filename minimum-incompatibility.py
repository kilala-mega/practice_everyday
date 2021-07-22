"""

"""
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums)//k
        @lru_cache(None)
        def solve(nums):
            if not nums:
                return 0
            res = float('inf')
            for comb in combinations(set(nums), d):
                left = list(nums)
                for c in comb:
                    left.remove(c)
                diff = max(comb) - min(comb)
                if diff > res: 
                    continue
                res = min(res, diff + solve(tuple(left)))
            return res
        res = solve(tuple(nums))
        return res if res != float('inf') else -1
        
