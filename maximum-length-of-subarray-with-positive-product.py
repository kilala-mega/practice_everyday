"""
a subarray with positive product means no 0, even count of negative elements
maximum length

"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = [0]*len(nums), [0]*len(nums)
        # longest subarray ending on i-th element with +/- product
        # result is max(pos)
        # pos[i] = pos[i-1] if nums[i] > 0 neg[i-1] if nums[i]<0 0 if nums[i] == 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > 0:
                    pos[0] = 1
                elif nums[i] < 0:
                    neg[0] = 1
            else:
                if nums[i] > 0:
                    pos[i] = 1+pos[i-1]
                    neg[i] = 1+neg[i-1] if neg[i-1] > 0 else 0
                elif nums[i] < 0:
                    pos[i] = neg[i-1]+1 if neg[i-1] > 0 else 0
                    neg[i] = pos[i-1]+1
                else:
                    pos[i] = 0
                    neg[i] = 0
        return max(pos)
        
