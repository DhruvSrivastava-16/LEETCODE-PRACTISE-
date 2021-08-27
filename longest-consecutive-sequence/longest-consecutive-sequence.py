class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        
        
        longest = 1
        temp = 1
        for i in range(0,len(nums)-1):
            
            if nums[i+1]!=nums[i]:
                if nums[i+1] - nums[i]==1: 
                    temp += 1
                
                else:
                    longest = max(longest,temp)
                    temp=1
                
            
                
        return max(longest,temp)