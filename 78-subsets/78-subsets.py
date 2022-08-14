class Solution:
    
    def bt(self,sz,ans,temp,pos,nums):
        if len(temp)==sz:
            ans.append(temp[:])
            return 
        
        for itr in range(pos,len(nums)):
            temp.append(nums[itr])
            self.bt(sz,ans,temp,itr+1,nums)
            temp.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        temp = []
        ans = []
        for sz in range(0,len(nums)+1):
            temp = []
            self.bt(sz,ans,temp,0,nums)
            
        return(ans)