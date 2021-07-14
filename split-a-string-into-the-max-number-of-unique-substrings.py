"""
a -> 1
aa, aaa -> 1
gcg -> 2
set to record current substrings
path = ""
try one character first, if already exists, add it to path and continue 
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrace(s, seen)
    def backtrace(self, s: str, seen: Set[str]) -> int:
        ans = 0
        if s:
            for i in range(1, len(s)+1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    ans = max(ans, 1 + self.backtrace(s[i:], seen))
                    seen.remove(candidate)
        return ans
    
        
