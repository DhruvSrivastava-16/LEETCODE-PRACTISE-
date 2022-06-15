class Solution:
    def bs(self,nums,l,h):
        if l==h:
            return l
        
        mid = (l+h)//2
        if nums[mid]>nums[mid+1]:
            return self.bs(nums,l,mid)
        
        return self.bs(nums,mid+1,h)
        
    def findPeakElement(self, nums: List[int]) -> int:
        return self.bs(nums,0,len(nums)-1)