class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        i, j, sum1, sum2 = 0, 0, 0, 0
        res = 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                res += max(sum1, sum2) + nums1[i]
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
        
        while i < m:
            sum1 += nums1[i]
            i += 1
        while j < n:
            sum2 += nums2[j]
            j += 1
        return (res + max(sum1, sum2)) % (10**9 + 7)
