class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zprod = 1
        cz = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                prod *= nums[i]
            
            if nums[i]==0:
                cz+=1
                
        if cz>1:
            return [0 for n in nums]
            
        print(prod)
        for n in range(len(nums)):
            
            if cz == 1:
                if nums[n]==0:
                    nums[n] = prod

                else:
                    nums[n] = 0
            
            else:
                nums[n] = prod//nums[n]
            
        return nums