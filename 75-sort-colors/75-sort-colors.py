class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        
        itr = 0
        
        while itr<=p2:
            
            if nums[itr]==2:
                nums[itr], nums[p2] = nums[p2], nums[itr]
                p2-=1
                
                
            elif nums[itr]==0:
                nums[itr], nums[p0] = nums[p0], nums[itr]
                p0+=1
                itr+=1
                
            else:
                itr+=1
            
        print(nums)