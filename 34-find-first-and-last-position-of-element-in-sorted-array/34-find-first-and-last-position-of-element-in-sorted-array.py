class Solution:
    
    def binarySearch(self, nums, target, low, high, pos):
        lowest, highest = -1, -1
        
        
        while low<=high:
            
            mid = (low+high)//2
            
            if nums[mid]==target and mid not in pos:
                
                pos.add(mid)
                
                self.binarySearch(nums, target, low, mid-1, pos)
                self.binarySearch(nums, target, mid+1, high, pos)
                
            elif nums[mid] < target:
                
                low = mid+1
                
            else:
                
                high = mid-1
                
                
            
 
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(nums)-1
        pos = set()
        
        self.binarySearch(nums, target, low, high, pos)
        
        if len(pos)==0:
            
            return [-1,-1]
        
        else:
            
            return [min(pos), max(pos)]
        