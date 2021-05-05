class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, n in enumerate(nums):
            if i > reachable:
                return False
            reachable = max(reachable, i + n)
        return reachable >= len(nums)-1
