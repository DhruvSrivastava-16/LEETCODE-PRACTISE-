class Solution:
    def findMax(self, stk, pos):
        maxPos = pos
        maxx = stk[pos]
        for i in range(pos,len(stk)):
            if maxx <= stk[i]:
                maxPos = i
                maxx = stk[i]
                
        return maxPos
        
    
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        stk = []
        for itr in num:
            stk.append(int(itr))
            
        num = int(num) 
        
        for i in range(len(stk)):
            gotP = self.findMax(stk,i)
            if gotP==i:
                continue
                
            elif stk[gotP]!=stk[i]:
                stk[i], stk[gotP] = stk[gotP], stk[i]
                ans = ''
                for i in stk:
                    ans+=str(i)
                    
                return int(ans)
                
                
        return num