class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        lower = 0
        higher = 0
        
        store = None
        curr = 0
        answer = 0
        Flag = False
        zr = 0
        
        while higher<len(nums):
            
            if nums[higher]==0:
                zr+=1
                
                while zr==2:
                    if nums[lower]==0:
                        zr-=1
                    lower+=1

                    
            higher+=1
            
            answer = max(answer,higher-lower)
            
        return(answer)
                
                