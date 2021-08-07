class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0 
        right_ptr = len(height)-1
        
        curr_max = 0
        
        while left_ptr<=right_ptr:
            
            temp_max = (right_ptr-left_ptr)*min(height[right_ptr],height[left_ptr])
            
            if temp_max>=curr_max:
                curr_max = temp_max
                
            
            if height[right_ptr]>height[left_ptr]:
                left_ptr+=1
                
            else:
                right_ptr-=1
                    
        return(curr_max)
                
        