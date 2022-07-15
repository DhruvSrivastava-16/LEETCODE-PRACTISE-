class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        answer = 0
        zeros = 0
        
        while right<len(nums):
            
            if nums[right]==0:
                
                zeros += 1
                
                while zeros == k+1:
                    
                    if nums[left]==0:
                        zeros-=1
                    
                    left+=1
                    
            right+=1
            answer = max(answer,right-left)
            
        return answer