class Solution:
    def firstUniqChar(self, s: str) -> int:
        ap = {}
        
        for i in s:
            if i not in ap:
                ap[i] = 1
                
            else:
                ap[i] +=1
                
        ans = [[k,v] for k,v in ap.items() if v==1]
        
        if len(ans) == 0:
            return -1
        
        else:
            o = ans[0][0]
            
        print(ans,o)
        
        ct = 0
        for i in s:
            if i==o:
                return ct
            ct+=1
            
        