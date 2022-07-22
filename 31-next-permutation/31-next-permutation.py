class Solution:
    
    def revArr(self,nums,left,right):
        

        
        while left<=right:
            
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
            
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)==1:
            return nums
        
        Found = False
        
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                Found = True
                break
                
        smaller = nums[i-1]
        smallerPos = i-1
                
        if not Found:
            self.revArr(nums,0,len(nums)-1)
            return 
        
        curr = float('inf')
        currPos = 0
        
        for i in range(smallerPos+1,len(nums)):
            
            if nums[i]>smaller and nums[i]<=curr:
                curr = nums[i]
                currPos = i
         
        nums[currPos], nums[smallerPos] = nums[smallerPos], nums[currPos]
        
        self.revArr(nums,smallerPos+1,len(nums)-1)
        
        return nums
                
        
                