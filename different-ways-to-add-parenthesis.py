class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @functools.lru_cache(None)
        def search(start:int, end:int) -> List[int]:
            res = []
            if end-start == 1:
                res.append(int(tokens[start]))
                return res
            for k in range(start+1, end, 2):
                op = tokens[k]
                l = search(start,k)
                r = search(k+1,end)
                if op == "+":
                    for i in l:
                        for j in r:
                            res.append(i+j)
                elif op == "-":
                    for i in l:
                        for j in r:
                            res.append(i-j)
                else:
                    for i in l:
                        for j in r:
                            res.append(i*j)
            return res
        tokens = [""]
        for i in range(len(expression)):
            if expression[i] not in "+-*":
                tokens[-1]+= expression[i]
            else:
                tokens.append(expression[i])
                tokens.append("")
        res = search(0, len(tokens))
        return res
        
