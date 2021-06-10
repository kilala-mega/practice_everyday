"""
left element, range

"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []
        currentMax = float('-inf')
        for i in range(len(nums)):
            h.append((nums[i][0], i, 0))
            currentMax = max(currentMax, nums[i][0])
        heapq.heapify(h)
        currentRange = float('inf')
        ret = [0,0]
        
        while len(h) >= len(nums):
            cur, row, col = heappop(h)
            if currentRange > currentMax - cur:
                currentRange = currentMax - cur
                ret[0] = currentMax - currentRange
                ret[1] = currentMax
            if col + 1 < len(nums[row]):
                currentMax = max(currentMax, nums[row][col+1])
                heappush(h, (nums[row][col+1], row, col+1))
        
        return ret
        
