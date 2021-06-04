"""
aeiou
for each of the vowels, ^mask with 1 << (ord(vowels) - ord('a'))
even counts of vowels means equal mask value
iterate the whole string
use a hash map to record the first occurence of each mask value
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        res = 0
        mask = 0
        loc = {0:-1}
        
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= 1 << (ord(s[i])-ord('a'))
            if mask in loc:
                res = max(res, i-loc[mask])
            else:
                loc[mask] = i
        return res
        
        
        
