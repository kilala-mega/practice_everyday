class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        ans = float('inf'), None, None
        
        while r < len(s):
            window_counts[s[r]] += 1
            if s[r] in dict_t and window_counts[s[r]] == dict_t[s[r]]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                window_counts[s[l]] -= 1
                if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]
