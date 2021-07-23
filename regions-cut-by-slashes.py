# divide a square into 4 triangular 
#  ----------
#  | \ 0  / |
#  | 1 \/ 2 |
#  |   /\   |
#  | /  3 \ |
#  ----------
# if grid[i][j] is / or ' ' then union 0 and 1, union 2 and 3
# if grid is \ or ' ', union 0 and 2, union 1 and 3
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.p[xroot] = yroot
        
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        dsu = DSU(4*N*N)
        
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                root = 4*(r*N + c)
                val = grid[r][c]
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)
                
                if r >= 1:
                    dsu.union(root + 0, root - 4*N + 3)
                if r < N-1:
                    dsu.union(root + 3, root + 4*N + 0)
                if c >= 1:
                    dsu.union(root + 1, root -4 + 2)
                if c < N-1:
                    dsu.union(root + 2, root + 4 +1)
        return sum(dsu.find(x)==x for x in range(4*N*N))
        
