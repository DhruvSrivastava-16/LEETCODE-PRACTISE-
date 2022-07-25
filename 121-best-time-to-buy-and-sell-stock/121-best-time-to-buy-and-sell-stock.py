class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = float('inf')
        currMax = -float('inf')
        
        answer = -float('inf')
        
        for i in range(0,len(prices)):
            
            if prices[i]<currMin:
                currMin = prices[i]
                
            elif prices[i]-currMin>answer:
                answer = prices[i]-currMin
                
             
        return max(answer,0)
                