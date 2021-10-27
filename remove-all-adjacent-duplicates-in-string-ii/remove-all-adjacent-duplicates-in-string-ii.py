class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stk = []
        
        for i in range(0,len(s)):
            
            if not stk:
                print(stk)
                stk.append([s[i],1])
                
            else:
                if stk[-1][0] == s[i]:
                
                    stk[-1][1] += 1
                    
                else:
                    stk.append([s[i],1])
                    
            if stk:
                if stk[-1][1]>=k:
                    stk.pop()
                    
        print(stk)
        
        ans = ''
        
        for s in stk:
            
            ans += s[0]*s[1]
            
        return ans
        