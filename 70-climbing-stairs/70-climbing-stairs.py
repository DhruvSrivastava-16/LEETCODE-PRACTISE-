class Solution:
    
    def BT(self,n,pos,i,memo,viSet):
        if pos in viSet:
            memo[i] += memo[pos]
            viSet.add(i)

            return 
        
        if pos == n:
            memo[i]+=1
            viSet.add(i)
            return 
        
        if pos +1 <=n:
            self.BT(n,pos+1,i,memo,viSet)
            
        if pos +2 <=n:
            self.BT(n,pos+2,i,memo,viSet)
        
    
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(0,n+1)]
        visSet = set()
        for j in range(n,-1,-1):
            self.BT(n,j,j,memo,visSet)
            
        return(memo[0])