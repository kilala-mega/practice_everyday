"""
nums
k > 0
competitive subsequence 
the most competitive

the 1st element of the result must be the smallest number in the array
to prove: if it's not, then there is other subseq with a smaller 1st element. then it should be the result
unless the smallest number is between location len(nums)-k+1 len(nums)-1
index(nums, min(nums[len(nums)-k+1:]))
we first find the smallest number in the array, find its index (leftmost)
the following k-1 elements will be on its right
similarly to finding the remaining k-1 elements
O(n*k)
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        additional_count = len(nums) - k
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and additional_count > 0:
                stack.pop()
                additional_count -= 1
            stack.append(nums[i])
        return stack[:k]
