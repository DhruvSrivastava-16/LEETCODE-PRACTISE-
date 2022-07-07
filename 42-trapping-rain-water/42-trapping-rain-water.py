class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxl = height[l]
        maxr = height[r]
        ans = 0
        while l < r:
            
            if maxl <= maxr:
                c = min(maxl, maxr) - height[l]
                if c > 0:
                    ans+=c
                l+=1
                maxl = max(maxl, height[l])
            else:
                c = min(maxl, maxr) - height[r]
                if c > 0:
                    ans+=c
                r-=1
                maxr = max(maxr, height[r])
        return ans