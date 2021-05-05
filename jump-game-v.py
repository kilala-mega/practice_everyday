import functools
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def jump(index: int) -> int:
            res = 0
            for direction in [-1,1]:
                for x in range(1,d+1): # this is important to ensure value between i j is < arr[i]
                    nextidx = x * direction + index
                    if 0 <= nextidx < len(arr) and arr[nextidx] < arr[index]:
                        res = max(res, jump(nextidx))
                    else:
                        break
            return res + 1
        return max([jump(i) for i in range(len(arr))])
