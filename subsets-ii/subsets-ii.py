class Solution:
    def gen(self,sz,st,temp,nums):
        if len(temp)==sz:
            if temp not in self.ans:
                self.ans.append(temp[:])
            return
            
        for i in range(st,len(nums)):
            temp.append(nums[i])
            self.gen(sz,i+1,temp,nums)
            temp.pop()
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        for s in range(len(nums)+1):
            temp = []
            self.gen(s,0,temp,nums)
            
        return(self.ans)
        
        
        