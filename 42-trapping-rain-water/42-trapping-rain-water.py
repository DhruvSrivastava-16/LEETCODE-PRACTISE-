class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxL = height[left]
        maxR = height[right]
        
        itr = 0
        answer = 0
        
        while left<right:
            
            if maxL<maxR:
                
                
                temp = maxL-height[left]
                
                if temp>0:
                    answer+=temp
                    
                left+=1
                
                maxL = max(maxL,height[left])
                
            else:
                
    
                temp = maxR-height[right]
                
                if temp>0:
                    answer+=temp
                    
                right-=1
                
                maxR = max(maxR,height[right])
                
            
        return answer
            
            
            