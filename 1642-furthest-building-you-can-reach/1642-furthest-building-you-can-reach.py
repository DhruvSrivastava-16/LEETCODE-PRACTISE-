class Solution:
    
    def helper(self,heights,idx,bricks,ladders):
        
        climbs = []
        for i in range(1,len(heights[:idx+1])):
            if heights[i]-heights[i-1]>0:
                climbs.append(heights[i]-heights[i-1])
                
        climbs.sort()
        
        bricks_remaining = bricks
        ladders_remaining = ladders
        for climb in climbs:
            # If there are enough bricks left, use those.
            if climb <= bricks_remaining:
                bricks_remaining -= climb
            # Otherwise, you'll have to use a ladder.
            elif ladders_remaining >= 1:
                ladders_remaining -= 1
            # And if there are no ladders either, we can't reach buildingIndex.
            else:
                return False
        return True
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lo = 0
        hi = len(heights) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.helper(heights,mid,bricks,ladders):
                lo = mid
            else:
                hi = mid - 1
        return hi # Note that return lo would be equivalent. 

            