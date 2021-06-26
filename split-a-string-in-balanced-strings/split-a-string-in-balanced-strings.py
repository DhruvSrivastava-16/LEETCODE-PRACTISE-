class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cl = 0
        cr = 0
        total = 0
        for i in range(0,len(s)):
            if s[i] == 'L':
                cl +=1
            
            elif s[i] == 'R':
                cr +=1
            
            if cl == cr:
                total += 1
                
        return total