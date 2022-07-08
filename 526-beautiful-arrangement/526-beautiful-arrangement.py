class Solution:
    
    def backtrack(self,nums,loc,temp,answer,visited):
        
        if len(temp)==len(nums):
            answer.append(temp[:])
            return 
        
        for i in range(0,len(nums)):
            if i not in visited and (nums[i]%(len(temp)+1)==0 or (len(temp)+1)%nums[i]==0) :
                visited.add(i)
                temp.append(nums[i])

                self.backtrack(nums,i,temp,answer,visited)
                temp.pop()
                visited.remove(i)
            
            
        
    
    def countArrangement(self, n: int) -> int:
        
        nums = [i for i in range(1,n+1)]
        temp = []
        answer = []
        visited = set()
        
        for j in range(0,len(nums)):
            visited = set()
            temp = []
            
            if nums[j]%(1)==0 or 1%nums[j]==0:
                temp.append(nums[j])
                visited.add(j)
                self.backtrack(nums,j,temp,answer,visited)
                visited.remove(j)
            
        return (len(answer))