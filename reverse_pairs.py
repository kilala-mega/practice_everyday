class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        if not nums:
            return 0
        n = len(nums)
        def merge(s, e):
            if s >= e:
                return 0
            mid = (s+e)//2
            count = merge(s, mid) + merge(mid+1, e)
            l,r = s, mid+1
            j = mid+1
            for i in range(s, mid+1):
                while j <= e and nums[i]/2.0 > nums[j]:
                    j+=1
                count += (j - mid - 1)
            nums[s:e+1] = sorted(nums[s:e+1])
            return count        
                
        return merge(0, n - 1)
