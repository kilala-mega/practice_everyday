class Solution:
    def jump(self, nums: List[int]) -> int:
        count, currentJumpEnd, furtherest = 0, 0, 0
        n = len(nums)
        for i in range(n-1):
            furtherest = max(furtherest, i + nums[i])
            if i == currentJumpEnd:
                count += 1
                currentJumpEnd = furtherest
        return count
