class Solution:
    
    def findMaxCont(self,arr,st,end):
        
        if len(arr)==1:
            print('returning:',max(arr[0],end-arr[0]))
            return max(arr[0],end-arr[0])
        
        maxx = max(arr[0],end-arr[-1])
    
        for i in range(1,len(arr)):
            
            maxx = max(maxx,arr[i]-arr[i-1])
                
        return maxx
            
            
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        ver = self.findMaxCont(verticalCuts,0,w)
        hor = self.findMaxCont(horizontalCuts,0,h)
        
        return (ver*hor)% (10**9 + 7)