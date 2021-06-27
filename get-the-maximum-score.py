class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        modulo = 10**9 + 7
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        sum1, sum2 = 0, 0
        res = 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # nums1[i] == nums2[j]
                res += max(sum1, sum2) + nums1[i] # or nums2[j]
                i += 1
                j += 1
                sum1, sum2 = 0, 0
        
        while i < m:
            sum1 += nums1[i]
            i += 1
        
        while j < n:
            sum2 += nums2[j]
            j += 1
        
        res += max(sum1, sum2)%modulo
        
        return res%modulo
        
