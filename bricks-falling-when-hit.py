class DSU:
    def __init__(self, R, C):
        # the last node R*C is a dummy node for top nodes to connect to
        self.par = [i for i in range(R*C+1)] # parent node, originally point to itself
        self.rnk = [0] * (R*C + 1) # bigger one is the root
        self.sz = [1] * (R*C + 1) # component size
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x]) # updating while looking up
        return self.par[x]
    
    def union(self, x, y):
        # union 2 node
        xr, yr = self.find(x), self.find(y) # find the root for both
        if xr == yr:
            return
        if self.rnk[xr] < self.rnk[yr]:
            yr, xr = xr, yr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        
    def size(self, x):
        return self.sz[self.find(x)]
    
    def top(self):
        return self.size(len(self.sz)-1)-1 # meaning self.size(R*C)-1
    
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        
        def index(r: int, c: int)-> int:
            return r*C + c
        
        def neighbors(r: int, c: int):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        after = [row[:] for row in grid]
        for i, j in hits:
            after[i][j] = 0
        
        dsu = DSU(R,C)
        for r, row in enumerate(after):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C) # top row brick is stable
                    if r and after[r-1][c]:
                        dsu.union(i, index(r-1,c))
                    if c and after[r][c-1]:
                        dsu.union(i, index(r, c-1))
                    
        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if after[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                after[r][c] = 1
                add_on = max(0, dsu.top() - pre_roof - 1) # minus the block itself
                ans.append(add_on)
        return ans[::-1]
        
        
        
