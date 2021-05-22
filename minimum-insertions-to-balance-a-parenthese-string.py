class Solution:
    def minInsertions(self, s: str) -> int:
        rightNeeded, res = 0, 0
        for c in s:
            if c == ")":
                if rightNeeded > 0:
                    rightNeeded -= 1
                else:
                    res += 1
                    rightNeeded += 1
            elif c == "(":
                if rightNeeded % 2 == 1:
                    res += 1
                    rightNeeded -= 1
                rightNeeded += 2
            else:
                raise
            
        return res + rightNeeded
