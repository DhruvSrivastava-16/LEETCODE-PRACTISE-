class Solution:
    
    def dfs(self,node,balances):
        
        if node == len(balances):
            return 0
        
        if balances[node]==0:
            return self.dfs(node+1,balances)
        
        currBalance = balances[node]
        minSteps = float('inf')
        for n in range(node+1,len(balances)):
            
            if currBalance*balances[n]<0:
                
                balances[n]+=currBalance
                minSteps = min(minSteps,1+self.dfs(node+1,balances))
                balances[n]-=currBalance
        
        return minSteps
    
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        
        totalBalances = defaultdict(int)
        for transaction in transactions:
            
            totalBalances[transaction[0]]-=transaction[2]
            totalBalances[transaction[1]]+=transaction[2]
            
        balances = [v for k,v in totalBalances.items() if v!=0]
        
        if len(balances) == 0:
            return 0
            
        ans = self.dfs(0,balances)
        
        return ans