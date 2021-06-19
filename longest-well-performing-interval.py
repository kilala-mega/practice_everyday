"""
tiring day: hours[i] > 8
well-performing interval: # of tiring day > # of non-tiring days
# of tiring day - # of non-tiring days > 0
keep track of # of tiring day - # of non-tiring days
calculate the # of tiring day of hours[i:j] O(j-i)
O(n^2) algo

1 1 -1 -1 -1 -1 1 

"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        presum = 0
        seen = {}
        ans = 0
        for i, h in enumerate(hours):
            presum += 1 if h > 8 else -1
            if presum > 0:
                ans = i + 1
            if presum - 1 in seen:
                ans = max(ans, i-seen[presum-1])
            if presum not in seen:
                seen[presum] = i
        return ans
        
