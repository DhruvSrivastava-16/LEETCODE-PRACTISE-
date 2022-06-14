class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        currMax = -float('inf')
        for i in range(len(heights)-1,-1,-1):
            
            if heights[i]>currMax:
                ans.append(i)
                
            currMax = max(currMax,heights[i])
            
        ans.sort()
        return(ans)