class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right  = 0 
        store = dict()
        maxxSum = 0
        tempSum = 0
        
        while right<len(nums):

            if nums[right] in store:

                while nums[right] in store:
                    store.pop(nums[left])
                    tempSum-=nums[left]
                    left+=1
                            
                
            store[nums[right]] = right
                
            tempSum+=nums[right]
            maxxSum = max(maxxSum,tempSum)
            right+=1
            
        return maxxSum