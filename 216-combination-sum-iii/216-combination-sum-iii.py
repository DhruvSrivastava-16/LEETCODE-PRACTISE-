class Solution:
    def comb(self,temp,store,nums,k,n,pos,summ):
        if len(temp)==k and summ==n:
            store.append(temp[:])
            return 
        
        for i in range(pos,len(nums)):
            if summ+nums[i]>n:
                break
            
            temp.append(nums[i])
            summ+=nums[i]
            self.comb(temp,store,nums,k,n,i+1,summ)
            temp.pop()
            summ-=nums[i]   
            
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [i for i in range(1,10)]
        temp = []
        store = []
        summ = 0
        
        self.comb(temp,store,nums,k,n,0,summ)
        
        return(store)
        