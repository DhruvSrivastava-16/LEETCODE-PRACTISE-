class Solution:
    def reverse(self,arr,pos):
        end = len(arr)-1
        
        while pos<end:
            arr[pos], arr[end] = arr[end], arr[pos]
            pos+=1
            end-=1
            
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r_itr = len(nums)-2
        
        while r_itr>=0 and nums[r_itr+1]<=nums[r_itr]:
            r_itr-=1
            
        if r_itr>=0:
            j = len(nums)-1
            while(nums[j]<=nums[r_itr]):
                j-=1
                
            nums[r_itr], nums[j] = nums[j], nums[r_itr]
            
        print(nums)
        self.reverse(nums,r_itr+1)
        
        print(nums)
            