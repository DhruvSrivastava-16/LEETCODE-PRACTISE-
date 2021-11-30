class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        MP = [0 for i in range(len(prices)+2)]
        
        for i in range(len(prices)-1,-1,-1):
            
            C1 = 0
            
            for sell in range(i+1,len(prices)):
                
                prof = (prices[sell]-prices[i]) + MP[sell+2]
                C1 = max(prof,C1)
                
                
                
            C2 = MP[i+1]
            
            
            MP[i] = max(C1,C2)
            
            
        return MP[0]