class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = 0
        ptr_t = 0
        ans = ''
        
        for ptr_t in range(0,len(t)):
            if ptr_s<len(s) and s[ptr_s]==t[ptr_t]:
                ans = ans+s[ptr_s]
                ptr_s +=1
                
        print(ans)
        if ans==s:
            return True
        
        return False
                
        