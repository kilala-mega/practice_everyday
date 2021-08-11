# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col, idx = 0, 0, -1
        while idx == -1 or idx > 40:
            row = rand7()
            col = rand7()
            idx = col + (row-1)*7
            
        return 1 + (idx-1)%10
