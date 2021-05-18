'''
(()(()))
(1(1
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    newVal = 0
                    while stack and stack[-1] != "(":
                        addOn = stack.pop()
                        newVal += addOn 
                    stack.pop() # pop (
                    stack.append(2*newVal)
                                   
        return sum(stack)
        
