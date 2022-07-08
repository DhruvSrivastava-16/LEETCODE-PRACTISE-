class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalRight = sum(nums)-nums[0]
        totalLeft = 0
        itr = 0
        
        while itr<len(nums):
            
            if totalRight==totalLeft:
                return itr
            
            itr+=1
            if itr>=len(nums):
                return -1
            totalRight -= nums[itr]
            totalLeft += nums[itr-1]
        
        return -1
            