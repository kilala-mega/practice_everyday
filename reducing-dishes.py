'''
chef cook dishes
satisfaction level -> n dishes
cook any dish in 1 unit of time
like-time coefficient of a dish: time[i] * satisfaction[i] time[i] including previous dishes
return max sum of like-time coefficient

how to sort and select dishes to maximum sum
if +, then put larger one at later time -> gain more
if -, then either prepare it earlier or discard it
whether to prepare of discard -> depend on whether it will worth it to more time[i] to + dishes
worth it means abs(time * -dish) < abs((time+1)*+dishes) - abs(time* +dishes)
'''
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        res = 0
        
        for i in range(len(satisfaction)-1,-1,-1):
            # if worth it, add the dish to menu
            if total + satisfaction[i] > 0:
                total += satisfaction[i]
                res += total
        
        return res
        
