class Solution:

    def __init__(self, w: List[int]):
        self.presum = []
        self.total = sum(w)
        presum = 0
        for weight in w:
            presum += weight
            self.presum.append(presum)

    def pickIndex(self) -> int:
        temp = self.total * random.random()
        idx = bisect_left(self.presum, temp)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
