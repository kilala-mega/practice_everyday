'''
k * target = sum(nums)
if target is not an integer, then false
if we are able to find (k-1) subsets with equal sum target, then true (the remaining subset sum 
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder != 0 or max(nums) > target:
            return False
        
        def canPartitionKSubsetsWithTarget(remaingroups: int, startIndex: int, currSum: int) -> bool:
            if remaingroups == 0:
                return True
            if currSum == target:
                return canPartitionKSubsetsWithTarget(remaingroups-1, 0, 0)
            for i in range(startIndex, len(nums)):
                if currSum + nums[i] > target or visited[i]:
                    continue
                visited[i] = True
                if canPartitionKSubsetsWithTarget(remaingroups, i+1, currSum+nums[i]):
                    return True
                visited[i] = False
            return False
                
        visited = [False]*len(nums)    
        return canPartitionKSubsetsWithTarget(k, 0, 0)
