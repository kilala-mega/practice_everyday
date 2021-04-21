class NumMatrix:
    # fenwick tree
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.nums = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.tree = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
                

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row+1
        while i < self.m+1:
            j = col+1
            while j < self.n+1:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumHelper(row2+1, col2+1) - self.sumHelper(row2+1, col1) - self.sumHelper(row1, col2+1) + self.sumHelper(row1, col1)
    
    def sumHelper(self, row: int, col: int) -> int:
        total = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
