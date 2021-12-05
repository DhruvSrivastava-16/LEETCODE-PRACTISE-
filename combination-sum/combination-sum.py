class Solution:
    def helper(self,temp,target,candidates,st):
        if sum(temp) == target:
            self.answer.append(temp[:])
            return 
        
        if sum(temp)>target:
            return 
        
        for i in range(st,len(candidates)):
            temp.append(candidates[i])
            self.helper(temp,target,candidates,i)
            temp.pop()
            
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.helper([],target,candidates,0)
        return self.answer