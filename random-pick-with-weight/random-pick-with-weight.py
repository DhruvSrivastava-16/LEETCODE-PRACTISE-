class Solution:

    def __init__(self, w: List[int]):
        self.ps = []
        rs = 0
        
        for n in w:
            rs+=n
            self.ps.append(rs)
        

    def pickIndex(self) -> int:
        temp = random.random()
        t_sum = self.ps[-1]
        t_sum = temp*t_sum
        
        for i in range(0,len(self.ps)):
            if t_sum<self.ps[i]:
                return i
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()