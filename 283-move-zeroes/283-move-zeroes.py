class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cz = 0
        for i in range(len(nums)):
            if nums[i]==0:
                cz+=1
                
        cp = 0
        
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[cp]=nums[j]
                cp+=1
                

        for itr in range(cp,len(nums)):
            nums[itr] = 0
            
        return nums
            
            
            