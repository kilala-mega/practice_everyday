class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # two pointer centered at k
        # left, right => k at first
        res = mini = nums[k]
        i, j, n = k, k, len(nums)
        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))
        return res
            
