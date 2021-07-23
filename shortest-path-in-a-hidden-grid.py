# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        grid = {}
        grid[(0,0)] = master.isTarget()
        # -1 block, 1 start, 2 end, 0 visited
        directions = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
        moveback = {'U':'D','D':'U','L':'R','R':'L'}
        self.foundTarget = False
        def dfs(x, y):
            for d, (dx, dy) in directions.items():
                newx, newy = x + dx, y + dy
                if master.canMove(d) and (newx, newy) not in grid:
                    master.move(d)
                    grid[(newx, newy)] = 1 if master.isTarget() else 0
                    dfs(newx, newy)
                    master.move(moveback[d])          
        dfs(0, 0)

        q = []
        q.append((0, 0, 0))
        visited = set()
        while q:
            x, y, step = q.pop(0)
            if grid[(x,y)] == 1:
                return step
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                newx, newy = x+dx, y+dy
                if (newx, newy) in grid and (newx,newy) not in visited:
                    visited.add((newx,newy))
                    q.append((newx,newy,step+1))
        return -1    

        
            
