class Solution:
    
    def bt(self,nums,temp,answer,numsC,keys):
        # print(nums,temp,answer)
        if len(temp)==len(nums):
            answer.append(temp[:])
            return 
        
        for i in keys:
            if numsC[i]!=0:
                numsC[i]-=1
                temp.append(i)
                self.bt(nums,temp,answer,numsC,keys)
                numsC[i]+=1
                temp.pop()
            
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        numsC = Counter(nums)
        keys = numsC.keys()
        temp = []

        self.bt(nums,temp,answer,numsC,keys)
            
        return(answer)