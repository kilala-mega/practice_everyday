class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = [start]
        visited.add(start)
        
        while queue:
            idx = queue.pop()
            if arr[idx] == 0:
                return True
            for j in [idx-arr[idx], idx+arr[idx]]:
                if 0<= j < len(arr) and j not in visited:
                    queue.append(j)
                    visited.add(j)
        return False
            
