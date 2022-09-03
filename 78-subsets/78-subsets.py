class Solution:
    
    def backtrack(self,size,loc,temp,answer,nums):
        if len(temp) == size:
            if temp not in answer:
                answer.append(temp[:])
            return
            
        
        
        for itr in range(loc,len(nums)):
            temp.append(nums[itr])
            self.backtrack(size,itr+1,temp,answer,nums)
            temp.pop()
            
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        temp = []
        
        for size in range(len(nums)+1):
            
            for loc in range(len(nums)):
                
                temp = []
                
                self.backtrack(size,loc,temp,answer,nums)
                
        return answer