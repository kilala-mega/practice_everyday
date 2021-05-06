class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        next_min_higher = [0] * n # index of next min higher
        next_max_lower = [0] * n # index of next max lower
        
        stack = []
        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_min_higher[stack.pop()] = i
            stack.append(i)
            
        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_max_lower[stack.pop()] = i
            stack.append(i)
         
        # think of it as boolean: can reach to index i by jumping higher/lower
        canReachByOddJump, canReachByEvenJump = [0]*n, [0]*n
        canReachByOddJump[-1] = 1 # last element can always reach itself
        canReachByEvenJump[-1] = 1
        
        for i in range(n-2,-1,-1): # iterate different starting points
            canReachByOddJump[i] = canReachByEvenJump[next_min_higher[i]]
            canReachByEvenJump[i] = canReachByOddJump[next_max_lower[i]]
        
        return sum(canReachByOddJump)
