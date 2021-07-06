class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.append(h)
        vc.append(w)
        hc.sort()
        vc.sort()
        
        maxh = hc[0]
        maxv = vc[0]
        
        
        for i in range(0,len(hc)-1):
            if hc[i+1] - hc[i] > maxh:
                maxh = hc[i+1] - hc[i]
                
        for i in range(0,len(vc)-1):
            if vc[i+1] - vc[i] > maxv:
                maxv = vc[i+1] - vc[i]
                
        
       
        return (maxv*maxh) % (10**9 + 7)
                
        
        