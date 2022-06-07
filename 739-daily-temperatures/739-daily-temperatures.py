class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
    
        ans = [0]
        stk = [(t[-1],len(t)-1)]
        
        for i in range(len(t)-2,-1,-1):
            if stk:
                if t[i]<stk[-1][0]:
                    ans.append((stk[-1][1]-i))
                    stk.append((t[i],i))
                    
                else:
                    while stk and stk[-1][0]<=t[i]:
                        stk.pop()
                    
                    if stk:
                        ans.append((stk[-1][1]-i))
                        stk.append((t[i],i))
                        
                    else:
                        ans.append(0)
                        stk.append((t[i],i))
                        
            else:
                
                ans.append(0)
                stk.append((t[i],i))
                
        return ans[::-1]