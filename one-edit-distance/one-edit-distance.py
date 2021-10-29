class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        sz_s = len(s)
        sz_t = len(t)
        
        if abs(sz_s-sz_t)>1:
            return False
        
        if sz_s<sz_t:
            smaller = s
            bigger = t
            
        else:
            smaller = t
            bigger = s
            
        
        for i in range(0,len(smaller)):
            if smaller[i]!=bigger[i]:
                if sz_s!=sz_t:
                    return smaller[i:]==bigger[i+1:]
                
                else:
                    return smaller[i+1:]==bigger[i+1:]
                
        return abs(sz_s-sz_t)==1