class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
        seen = set()
        lo, hi = 0, 0
        res = 0
        for hi,w in enumerate(word):
            if hi > 0 and word[hi] < word[hi-1]:
                # not in order
                seen = set()
                lo = hi
            seen.add(w)
            if len(seen) == 5:
                res = max(res, hi-lo+1)
        return res
        
        
