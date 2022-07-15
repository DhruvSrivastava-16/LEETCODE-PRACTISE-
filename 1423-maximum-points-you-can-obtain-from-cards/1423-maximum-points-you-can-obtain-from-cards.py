class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        window = len(cardPoints)-k
        
        low = 0
        high = 0
        minSum = sum(cardPoints)
        curSum = 0
        total = sum(cardPoints)
        
        if window<=0:
            return total
        
        while high<len(cardPoints):
            
                
            curSum+=cardPoints[high]
               

            if high-low+1==window:
                print(low,high,curSum)
                minSum = min(minSum,curSum)
                curSum -= cardPoints[low]
                low+=1
                
            high+=1
        
        print(total,minSum)       
        return (total-minSum)
            
            