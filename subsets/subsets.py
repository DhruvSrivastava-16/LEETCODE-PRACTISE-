class Solution:
    def helper(self,nums,sz,temp,st):
        if len(temp) == sz:
            self.ss.append(temp[:])
            return
            
        for i in range(st,len(nums)):
            temp.append(nums[i])
            self.helper(nums,sz,temp,i+1)
            temp.pop()

            
            
        
            
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ss = []
        temp = []
        for sz in range(0,len(nums)+1):
            self.helper(nums,sz,temp,0)
            
        
        return(self.ss)
            