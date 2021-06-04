"""
inventory - counter of ith color ball
orders - total number of ball
maximum value 
1st ball of each color is the most expensive ones but also the more the number of balls of 
same color, the more expensive the first ball and following balls are because the price of the first ball is determined by how many balls of same color in total
bruce force, find max(inventory), orders--, inventory[maxi]-- and iterate until orders == 0
        fn = lambda x: sum(max(0, xx - x) for xx in inventory) # balls sold 
    
        # last true binary search 
        lo, hi = 0, 10**9
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid) >= orders: lo = mid
            else: hi = mid - 1
        
        ans = sum((x + lo + 1)*(x - lo)//2 for x in inventory if x > lo)
        return (ans - (fn(lo) - orders) * (lo + 1)) % 1_000_000_007
"""
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        modulo = 10**9 + 7
        start, end = 0, max(inventory)
        def getScore(threshold):
            res = 0
            for i in range(len(inventory)):
                if inventory[i] > threshold:
                    # (threshold + 1) + ... + inventory[i]
                    res += (inventory[i]+threshold+1)*(inventory[i]-threshold)//2%modulo
            return res%modulo
        def getCount(threshold):
            res = 0
            for i in range(len(inventory)):
                if inventory[i] > threshold:
                    res += inventory[i]-threshold
            return res
        fn = lambda x: sum(max(0, xx - x) for xx in inventory) # balls sold
        while start + 1 < end:
            mid = (start + end)//2
            if fn(mid) >= orders:
                start = mid
            else:
                end = mid
                
        if fn(end) >= orders:
            return (getScore(end)- (fn(end) - orders) * (end + 1)) % 1_000_000_007
        elif fn(start) >= orders:
            return (getScore(start)- (fn(start) - orders) * (start + 1)) % 1_000_000_007
        else:
            return -1       
  

            
        
