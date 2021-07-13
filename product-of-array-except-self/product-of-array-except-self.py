class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        r = [0] * len(nums)
        ans = [0] * len(nums)
        
        l[0] = 1
        r[-1] = 1
        
        for i in range(1,len(nums)):
            l[i] = l[i-1] * nums[i-1]
            
        print(l)
         
        for i in range(len(nums)-2,-1,-1):
            print(i)
            r[i] = r[i+1] * nums[i+1]
            
        print(r)
            
        for i in range(0,len(nums)):
            ans[i] = l[i]*r[i]
            
        return ans
        
            
        