class Solution:
    def checkBA(self,p):
       
        for i in range(1,len(p)+1):
            if p[i-1]%i!=0 and i%p[i-1]!=0:
                return False
            
        return True
    
    def backtrack(self,first,nums,n,perms):
        if first == n:
            perms.append(nums[:])
            
            
        for i in range(first,n):
            nums[first],nums[i]=nums[i],nums[first]
            if nums[first]%(first+1)==0 or (first+1)%nums[first]==0:
                self.backtrack(first+1,nums,n,perms)
            nums[first],nums[i]=nums[i],nums[first]

        
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1,n+1)]
        first = 0
        perms = []
        
        self.backtrack(first,nums,n,perms)
    
        ans=0
        for p in perms:
            
            if(self.checkBA(p)):
                print(p)
                ans+=1
        
        return ans
        
        