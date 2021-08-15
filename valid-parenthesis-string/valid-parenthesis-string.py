class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        
        for i in s:
            if i=='(':
                lo+=1
                hi+=1
            
            if i=='*':
                lo-=1
                hi+=1
            
            if i==')':
                lo-=1
                hi-=1
                
            if hi<0:
                break
                
            lo = max(lo,0)
        
        print(lo,hi)
        return lo==0
                
                
                
                
            