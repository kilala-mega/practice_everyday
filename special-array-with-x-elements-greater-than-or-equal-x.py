    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if nums[0] < 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] >= i and nums[i] < i:
                return i
        if nums[-1] >= len(nums):
            return len(nums)
        return -1
