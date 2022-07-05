class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)
        
        if len(t)-len(s)>1:
            return False
        
        for i in range(ns):
            if s[i]!=t[i]:
                if ns==nt:
                    return s[i+1:]==t[i+1:]
                
                else:
                    return s[i:]==t[i+1:]
                
        return ns+1==nt