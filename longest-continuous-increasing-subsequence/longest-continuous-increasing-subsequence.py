class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_l = -1
        temp = 1
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                print(nums[i],nums[i-1],temp)
                temp+=1
                
            else:
                max_l = max(max_l,temp)
                temp = 1
                
        return max(max_l,temp)
            