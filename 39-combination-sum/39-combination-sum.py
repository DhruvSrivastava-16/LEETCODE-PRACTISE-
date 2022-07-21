class Solution:
    
    def backtrack(self,nums,temp,answer,target,tsum,st):
        
        if tsum == target:
            answer.append(temp[:])
            return 
        
        for i in range(st,len(nums)):
            if tsum+nums[i]>target:
                continue
                
            else:
                tsum+=nums[i]
                temp.append(nums[i])
                self.backtrack(nums,temp,answer,target,tsum,i)
                temp.pop()
                tsum-=nums[i]
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        self.backtrack(candidates,[],ans,target,0,0)
        return(ans)
        