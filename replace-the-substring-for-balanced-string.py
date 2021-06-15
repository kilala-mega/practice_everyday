"""
{qwer}
n/4 - n is len of string
qeerqrrr
qqwweerr  

because we can't have a character's count > n/4
if so, the extra ones should be replaced

therefore, we check count[key] <= n/4 for all 4 characters
if any of the character >n/4, we move right to remove s[right] from count
"""
class Solution:
    def balancedString(self, s: str) -> int:
        res = n = len(s)
        count = Counter(list(s))
        
        left, right = 0, 0
        while right < len(s):
            count[s[right]] -= 1
            right += 1
            # add s[right] to the sliding window
            print('right=', right, ' ', count)
            while left < len(s) and all(count[key] <= len(s)/4 for key in 'QWER'):
                # we can replace any characters in [left: right] but need count(qwer) out side the window to be <= n/4
                res = min(res, right - left) # right-1 - left + 1
                count[s[left]] += 1
                left += 1
        
        return res
        
        
