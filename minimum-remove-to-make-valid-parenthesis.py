class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bal = 0
        aux = ""
        for i in range(len(s)):
            if s[i] == "(":
                bal += 1
                aux += s[i]
            elif s[i] == ")":
                if bal > 0:
                    aux += s[i]
                    bal -= 1
            else:
                aux += s[i]
        if bal == 0:
            return aux
        i = len(aux)-1
        res = [""]*(len(aux)-bal)
        j = len(res)-1
        while i >= 0:
            if aux[i] == "(":
                if bal > 0:
                    bal -= 1
                else:
                    res[j] = aux[i]
                    j-=1
            else:
                res[j] = aux[i]
                j-=1
            i -= 1
        return "".join(res)
                    
