class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        prefixSum = 0
        nums.sort()
        ans = 0
        prefixSum =0
        total = 0
        
        left = 0
        right = 0
        
        while right<len(nums):
            
            prefixSum +=nums[right]

            while nums[right]*(right-left+1)>prefixSum + k:
                left+=1
                maxxSum = nums[right]*(right-left+1)
                prefixSum -=nums[left-1]
                    
                    
            ans = max(right-left+1,ans)
            right+=1
                    
        return ans