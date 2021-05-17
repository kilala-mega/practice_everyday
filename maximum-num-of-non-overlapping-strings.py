class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        def findRight(c:str, l:int, r:int) -> int:
            ans = -1
            j = l
            
            while j < len(s):
                if leftBoundry[s[j]] < l:
                    return -1
                ans = max(ans, rightBoundry[s[j]])
                j += 1
                if j > ans:
                    break
            return ans
        leftBoundry = {}
        rightBoundry = {}
        for i in range(len(s)):
            c = s[i]
            if c not in leftBoundry:
                leftBoundry[c] = i
            rightBoundry[c] = i
        res = []  
        right = -1
        for i in range(len(s)):
            c = s[i]
            l, r = leftBoundry[c], rightBoundry[c]
            if l != i:
                continue
            newright = findRight(c, l, r)
            if newright != -1:
                # append string or modify the last one
                if i > right:
                    res.append("")
                res[-1] = s[l:newright+1]
                right = newright
        
        return res
                
            
