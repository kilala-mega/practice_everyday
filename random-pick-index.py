class Solution:

    def __init__(self, nums: List[int]):
        self.positions = defaultdict(list)
        for i, n in enumerate(nums):
            self.positions[n].append(i)

    def pick(self, target: int) -> int:
        n = random.randint(0, len(self.positions[target])-1)
        return self.positions[target][n]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
