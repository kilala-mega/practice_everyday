"""
xor = 0 arr[i]^..arr[k]
find subarray with length >= 2
if found and the length is x, what is the count? given i<j<==k. j has x-1 options and for each j, k has x-j options
j = i+1, k has x-1
j = i+2, k has x-2
j = i+x-1, k has x-x+1
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if not arr or len(arr) <= 1:
            return 0
        arr = [0] + arr
        # calculate prefix xor prefix[i] = a[0]^...^a[i-1]
        for i in range(len(arr)-1):
            arr[i+1] ^= arr[i]
        res = 0   
        for i in range(len(arr)-1):
            for k in range(i+1, len(arr)):
                # i < j <= k. 
                if arr[i] == arr[k]:
                    # arr[i] == arr[k] means a[i]^a[i+1]..^a[k-1] = 0
                    # because i < j so add k-1-(i+1)+1
                    res += k-i-1
        return res
                    
