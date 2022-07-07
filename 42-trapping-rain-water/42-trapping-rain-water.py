class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        maxL = height[0]
        maxR = height[-1]
        
        totalStorage = 0
        
        while left<right:
            
            if maxL < maxR:
                
                temp = maxL-height[left]
                
                if temp>0:
                    totalStorage += temp
                    
                left+=1
                
                maxL = max(maxL,height[left])
                
            else:
                
                temp = maxR-height[right]

                if temp>0:
                    totalStorage += temp
                    
                right-=1
                
                maxR = max(maxR,height[right])
                
        return totalStorage