class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxL = height[0]
        maxR = height[-1]
        ans = 0
        
        while left<=right:
            
            if height[left]<height[right]:
                
                temp = maxL-height[left]
                
                if temp>0:
                    ans+=temp
                    
                maxL = max(maxL,height[left])
                left+=1
                
            else:
                
                temp = maxR -height[right]
                
                if temp>0:
                    ans+=temp
                    
                maxR = max(maxR,height[right])
                right-=1
                
        return ans