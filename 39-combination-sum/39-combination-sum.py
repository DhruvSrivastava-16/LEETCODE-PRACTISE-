class Solution:
    
    def combinations(self,temp,store,nums,summ,target,pos):
        
        if summ == target:
            store.append(temp[:])
            return 
        
        for i in range(pos,len(nums)):
            if summ+nums[i]>target:
                continue
                
            summ += nums[i]
            temp.append(nums[i])
            self.combinations(temp,store,nums,summ,target,i)
            summ -= nums[i]
            temp.pop()
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        temp = []
        store = []
        summ = 0
        self.combinations(temp,store,nums,summ,target,0)
        return(store)