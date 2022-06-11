class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {')':'(',']':'[','}':'{'}
        
        for i in s:
            
            if i in hmap:
                
                if stk and stk[-1] == hmap[i]:
                    stk.pop()
                    
                else:
                    return False
                
            else:
                stk.append(i)
                
        if len(stk)!=0:
            return False
        
        return True