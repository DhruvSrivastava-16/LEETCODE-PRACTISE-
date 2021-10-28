class Solution:
    def trap(self, height: List[int]) -> int:
        
        stk = []
        
        ans = 0
        dist = 0
        h = 0
        
        for i in range(0,len(height)):
            
            while stk and height[i]>height[stk[-1]]:
                
                top = stk.pop()
                if len(stk)==0:
                    break
                    
                h = min(height[i],height[stk[-1]])-height[top]
                dist = i - stk[-1]-1
                ans += dist*h
                
                
            stk.append(i)
        
        return ans


       