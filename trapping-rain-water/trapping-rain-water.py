class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        current = 0
        dist = 0
        ans = 0
        
        for i in range(0,len(height)):
            while len(stk)>0 and height[i]>height[stk[-1]]:
           
               
                top = stk.pop()
                if len(stk)==0:
                    break
                dist = i-stk[-1]-1
                h = min(height[i],height[stk[-1]])-height[top]
                ans+=dist*h
                    
            stk.append(i)
            
        return(ans)
       