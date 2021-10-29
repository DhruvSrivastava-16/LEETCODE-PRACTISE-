class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        sz_s = len(s)
        sz_t = len(t)
        
        if abs(sz_s-sz_t)>1:
            return False
        
        if sz_s>sz_t:
            smaller = t
            bigger = s
            
        else:
            smaller = s
            bigger = t
            
        print(smaller,bigger)
            
        for i in range(len(smaller)):
            print(i)
            if smaller[i]!=bigger[i]:
                if len(bigger) == len(smaller):
                    return smaller[i+1:]==bigger[i+1:]
                
                else:
                    return smaller[i:]==bigger[i+1:]
                
        return len(smaller)+1==len(bigger)