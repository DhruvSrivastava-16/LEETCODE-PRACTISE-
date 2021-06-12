class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999999
        max_prof = -999999
        j = 0
        l = len(prices)
        f = -1
        
        for i in range(1,l):
            
            if min_price > prices[j]:
                min_price = prices[j]
                
                
            if max_prof < prices[i] - min_price:
                f = 0
                max_prof = prices[i] - min_price
            
            j+=1
            
                
        if max_prof<0:
            return 0
        
        return max_prof
            
                
        