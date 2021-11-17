class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        lowest = -1
        
        while left<=right:
            
            mid = (left+right)//2
            
            if nums[mid] == target:
                lowest = mid
                right = mid - 1
                
            elif nums[mid]>target:
                right = mid-1
                
            else:
                left = mid+1
                
                
        left = 0
        right = len(nums)-1
        highest = -1
        
        while left<=right:
            
            mid = (left+right)//2
            
            if nums[mid] == target:
                highest = mid
                left = mid+1
                
            elif nums[mid]>target:
                right = mid-1
                
            else:
                left = mid+1
                
        
        return [lowest,highest]