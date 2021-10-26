class Solution:
    ans = []
    def helper(self,candidates,target,s,temp,start):
        if sum(temp)>target:
            return
        
        elif sum(temp)==target:
            t = tuple(temp)
            
            self.ans.append(temp[:])
            
        else:
            for j in range(start,len(candidates)):
                temp.append(candidates[j])
                #print(temp)
                self.helper(candidates,target,s,temp,j)
                temp.pop()
                
        
                
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        s = set()
      
        self.helper(candidates,target,s,[],0)
       
        return(self.ans)
        