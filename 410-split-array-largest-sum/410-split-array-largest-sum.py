class Solution:
    
    def bucketsRqd(self,nums,mid):
        needed = 1
        summ = 0
        
        for i in range(len(nums)):
            
            if nums[i]+summ>mid:
                needed+=1
                summ = nums[i]
                
            else:
                summ+=nums[i]
                
        return needed
                
        
        
    def splitArray(self, nums: List[int], m: int) -> int:
        
        left = max(nums)
        right = sum(nums)
        
        while left<=right:
            
            mid = (left+right)//2
            
            if self.bucketsRqd(nums,mid)<=m:
                right = mid-1
                answer = mid
                
            else:
                left = mid+1
                
        return answer
        
        