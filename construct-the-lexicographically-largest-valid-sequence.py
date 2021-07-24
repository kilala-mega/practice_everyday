class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2*n - 1) # total 2xn+1 numbers
        visited = set() # candidate 1 to n
        def dfs(index: int) -> List[int]:
            if len(visited) == n:
                return arr
            if arr[index] > 0:
                return dfs(index+1)
            for x in range(n, 0, -1):
                if x not in visited:
                    sec_index = index + x
                    if x == 1:
                        sec_index = index
                    if sec_index < len(arr) and arr[index] == 0 and arr[sec_index] == 0:
                        arr[index], arr[sec_index] = x, x
                        visited.add(x)
                        ans = dfs(index + 1)
                        if ans:
                            return ans
                        visited.remove(x)
                        arr[index], arr[sec_index] = 0, 0
        return dfs(0)
