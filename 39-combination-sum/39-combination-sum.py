class Solution:
    
    def backtrack(self,nums,answer,temp,target,summ,pos):
        if summ==target:
            answer.append(temp[:])
            return 
        
        for itr in range(pos,len(nums)):
            if nums[itr]+summ>target:
                break
            temp.append(nums[itr])
            self.backtrack(nums,answer,temp,target,summ+nums[itr],itr)
            temp.pop()
            
        return
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        temp = []
        summ = 0
        candidates.sort()
        
        self.backtrack(candidates,answer,temp,target,summ,0)
        
        return(answer)