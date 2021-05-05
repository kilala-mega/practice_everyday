class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos = defaultdict(list)
        for i, n in enumerate(arr):
            pos[n].append(i)
        visited = set()
        queue = [(0,0)]
        visited.add(0)
        n = len(arr)
        while queue:
            currpos, steps = queue.pop(0)
            if currpos == n-1:
                return steps
            for x in [currpos-1, currpos+1]:
                if 0 <= x < n and x not in visited:
                    queue.append((x, steps+1))
                    visited.add(x)
            for x in pos[arr[currpos]]:
                if x not in visited:
                    queue.append((x,steps+1))
                    visited.add(x)
            del pos[arr[currpos]]
                    
        return -1
