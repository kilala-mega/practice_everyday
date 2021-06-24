class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1):
            return -1
        if sum(nums1) < sum(nums2):
            nums1, nums2 = nums2, nums1
        # sum nums1 >= sum nums2
        nums1.sort()
        nums2.sort()
        
        ans = 0
        j = 0
        i = len(nums1)-1
        s1, s2 = sum(nums1), sum(nums2)
        
        while s1 > s2:
            if j >= len(nums2) or i >= 0 and nums1[i] > 6 - nums2[j] + 1:
                s1 -= nums1[i]-1
                i -= 1
            else:
                s2 += 6 - nums2[j]
                j += 1
            ans += 1
        return ans
        
