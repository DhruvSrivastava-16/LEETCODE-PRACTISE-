class Solution:
    def BT(self, sz, temp, pos,ans,nums):
        if sz==0:
            ans.append(temp[:])
            return
        
        for j in range(pos, len(nums)):
            temp.append(nums[j])
            self.BT(sz-1, temp, j+1,ans,nums)
            temp.pop()
            
        
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0,len(nums)+1):
            temp = []
            self.BT(i,temp,0,ans,nums)

        return ans