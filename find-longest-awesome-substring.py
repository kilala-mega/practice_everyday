"""
see constraints: s only contains digits
using bitmask to record odd/even number of a character
if the same bitmask appears again, this means in between the index1(exclusively) and the current index, the number of all chars are even.

"""
class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        res = 0
        
        dp = [-1] + 1023*[len(s)]
        for i in range(len(s)):
            mask ^= 1<<(ord(s[i])-ord('0'))
            res = max(res, i-dp[mask])
            for j in range(10):
                premask = mask ^ (1<<j)
                res = max(res, i-dp[premask])
            dp[mask] = min(dp[mask], i)
        
        return res
