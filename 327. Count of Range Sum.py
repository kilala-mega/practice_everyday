class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[i]+nums[i])
        
        hashmap = collections.defaultdict(int)
        count = 0
        for s in presum:
            for i in range(lower, upper+1):
                if s- i in hashmap:
                    count += hashmap[s-i]
            hashmap[s] += 1
        return count
