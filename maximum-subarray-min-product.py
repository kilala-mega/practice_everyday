"""
naive i j max O(n^3) space O(1)

min-product of a subarray nums[i:j]: 
sum of subarray -> prefix sum  with the cost of O(n) preprocessing
min value in nums[i:j] heap? no, higher cost of deleting elements by index


"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        module = 10**9 + 7
        if not nums:
            return 0
        presum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            presum[i+1] = nums[i] + presum[i]
        # sum(nums[i:j]) = presum[j] - presum[i]  
        left_bound = [0]*len(nums)
        right_bound = [len(nums)-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1][0]:
                _, idx = stack.pop()
                right_bound[idx] = i-1
            stack.append((nums[i], i))
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] < stack[-1][0]:
                _, idx = stack.pop()
                left_bound[idx] = i+1
            stack.append((nums[i], i))
        #print(left_bound, right_bound)
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i]*(presum[right_bound[i]+1]-presum[left_bound[i]]))
        
        return ans % module
        
            
        
        
        
        
