"""
if the num is odd, we can multiple by 2 -> then it become even -> can't increase more
if the num is even, we can not increase it. we can only decrease it by dividing by 2.

therefore, we can first increase the elements in the array to its maximum
and reduce them step by step

deviation = maxvalue - minvalue(known) -> minimize maxvalue 
add a the number to a maxheap
pop heap if it's an even number, divide it by 2 and add it back to heap
        else it's an odd number, return deviation
"""
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        for num in nums:
            if num % 2 == 0:
                # even number, can't increase 
                # we need a max heap, therefore push -num
                h.append(-num)
            else:
                # odd number
                h.append(-num*2)
        minValue = -max(h)
        res = float('inf')
        heapq.heapify(h)
        while h:
            cur = -heappop(h)
            res = min(res, cur-minValue)
            if cur%2 == 0:
                minValue = min(minValue, cur//2)
                heappush(h, -cur//2)
            else:
                break
        return res
        
