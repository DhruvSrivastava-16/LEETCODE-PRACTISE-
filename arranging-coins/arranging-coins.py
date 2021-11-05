class Solution:
    def arrangeCoins(self, n: int) -> int:
        maxx = 1
        for i in range(1,n):
            
            if i*(i+1)//2>n:
                
                break
                
            else:
                maxx = i
                
        return(maxx)