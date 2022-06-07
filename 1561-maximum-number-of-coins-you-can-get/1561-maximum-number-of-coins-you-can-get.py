class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        leftPtr = 0
        rightPtr = len(piles)-1
        alex, dhruv, bob = 0, 0 ,0
        
        while leftPtr+1 < rightPtr:
            
            alex += piles[leftPtr]
            dhruv += piles[leftPtr+1]
            bob += piles[rightPtr]
            
            leftPtr+=2
            rightPtr-=1
            
        return dhruv