class Solution:
    def backtrack(self,first, output, nums, n):
        if first == n:
            output.append(nums[:])
            
        for i in range(first,n):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(first+1, output, nums,n)
            nums[first],nums[i] = nums[i], nums[first]
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        first = 0
        self.backtrack(first,output,nums,n)
        return(output)