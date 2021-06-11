"""
time O(n**2) space O(n)
can improve to one pass
"""
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find(target, nums):
            seen = Counter() #use Counter so the default value is 0
            ret = 0
            for i in range(len(nums)):
                if target % nums[i] == 0:
                    ret += seen[target/nums[i]]
                seen[nums[i]] += 1
            return ret
        
        @lru_cache(None)
        def twoProduct1(target):
            return find(target, nums1)
        
        @lru_cache(None)
        def twoProduct2(target):
            return find(target, nums2)
        
        return sum(twoProduct2(a*a) for a in nums1) + sum(twoProduct1(a*a) for a in nums2)
