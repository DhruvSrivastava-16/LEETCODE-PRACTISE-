class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        Bmap  = {')':'('}
        
        for itr in s:
            
                
            if stk and itr == ')' and stk[-1] == '(':
                stk.pop()
                continue
                
            stk.append(itr)
            
        print(stk)
        
        return len(stk)
            