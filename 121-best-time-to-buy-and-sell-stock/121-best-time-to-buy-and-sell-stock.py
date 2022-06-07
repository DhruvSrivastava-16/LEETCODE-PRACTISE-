class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0
        
        for i in range(len(prices)):
            
            if minP > prices[i]:
                
                minP = prices[i]
                
            elif prices[i]-minP > maxP:
                
                maxP = prices[i]-minP
                
        return maxP