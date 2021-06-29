class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total = 0
        while len(sticks)>=2:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            c = a + b
            total = total + c
            heapq.heappush(sticks,c)
            
        return (total)
        