class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <1:
            return 0
        if len(stones) ==1:
            return stones[0]
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones)>=2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a == b:
                c=0
            else:
                a = a*(-1)
                b = b*(-1)
                c = a-b
            heapq.heappush(stones,-c)
            
        return -1*stones[0]
            