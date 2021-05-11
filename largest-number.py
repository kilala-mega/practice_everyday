class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sortedNum = sorted([str(num) for num in nums], key=cmp_to_key(lambda x, y: 1 if x + y < y+ x else -1))
        ans = "".join(sortedNum)
        startPos = 0
        while ans[startPos] == '0':
            if ans[startPos:] == "0":
                return ans[startPos:]
            startPos += 1
        return ans[startPos:]
        
