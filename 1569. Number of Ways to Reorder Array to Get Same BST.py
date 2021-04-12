class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # nodes in the same level can permutate
        # group nodes in different level 
        # another way is to group by left and right child 
        def helper(nums):
            if len(nums) <= 2:
                return 1
            smaller = [n for n in nums if n < nums[0]]
            greater = [n for n in nums if n > nums[0]]
            # comb(len(smaller)+len(greater), len(greater)) = comb(len(smaller)+len(greater), len(smaller))
            return comb(len(smaller)+len(greater), len(greater))*helper(smaller)*helper(greater)
        return (helper(nums) - 1)%(10 ** 9 + 7)
