class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        prev = None
        avoid = using = 0 # avoid current number, use current number
        
        for k in sorted(count):
            if k-1 != prev: # don't need to add k+1 because key is in order
                avoid, using = max(avoid, using), k*count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*count[k] + avoid
            prev = k
        return max(avoid, using)
        
