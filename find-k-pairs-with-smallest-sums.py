class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in range(min(k, len(nums1))):
            heappush(h, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        
        remaining = k
        res = []
        while h and remaining > 0:
            cur = heappop(h)
            res.append([cur[1], cur[2]])
            if cur[3] + 1 < len(nums2):
                heappush(h, (cur[1]+nums2[cur[3]+1], cur[1], nums2[cur[3]+1], cur[3]+1))
            remaining -= 1
        
        return res
        
