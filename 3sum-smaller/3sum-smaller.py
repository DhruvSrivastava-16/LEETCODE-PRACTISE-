class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        
        
        nums.sort()
        print(nums)
        left = 0
        right = 0
        ans = 0
        
        for i in range(len(nums)):
            
            curr = target - nums[i]
            
            left = i+1
            right = len(nums)-1
            
            while left<right and right>=0:
                
                
                if nums[left]+nums[right]>=curr:
                    right-=1
                
                else:
                    print(nums[i],nums[left],nums[right])
                    ans+=right-left
                    left+=1
                    
            
        return ans
                    
        