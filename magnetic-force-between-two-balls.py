"""
n baskets
ith basket at position[i]
m balls to distribute
minimum magnetic force between any two balls is maximum

magnetic force between 2 balls is abs(position[i]-position[j])
any two balls: n**2 combination
minimum value is the distance between two adjacent balls with smallest distance
put ball as far as each other
we are basically maximize the smallest distance among adjacent balls with limited choice of positions
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(step: int):
            cur = position[0]
            res = 1
            for i in range(1, len(position)):
                if position[i] - cur >= step:
                    res += 1
                    cur = position[i]
            return res
        start, end = 0, position[-1]
        while start + 1 < end:
            mid = (start + end)//2
            if count(mid) >= m:
                start = mid
            else:
                end = mid
        if count(end) >= m:
            return end
        elif count(start) >= m:
            return start
        else:
            return -1
            
