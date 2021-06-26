class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        diff = 0
        cn_o = 0
        cn_c = 0
        rq_o = 0
        tr = 0
        
        for i in s:
            if i == '(':
                cn_o += 1
            
            if i == ')':
                if cn_o > 0:
                    cn_o -= 1
                else:
                    rq_o += 1
                
        tr = rq_o + cn_o
        return tr
        