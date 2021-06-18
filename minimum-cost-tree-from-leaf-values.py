"""
arr[i] > 0
int
dp  max(arr[i:k] inclusive) x max(arr[k+1:j]) + dp[i:k] + dp[k+1:j]
dp[k:k] = arr[k]

"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i-1:i]+arr[i+1:i+2])*arr.pop(i)
        return res
        
