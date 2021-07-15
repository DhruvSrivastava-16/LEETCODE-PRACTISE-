class Solution:
    def countBits(self, n: int) -> List[int]:
        d = {0:0,1:1}
        for i in range(2,n+1):
            if i%2==0:
                d[i] = d[i//2]
            else:
                d[i] = d[i//2]+1
                         
        ans = []
        for i in range(0,n+1):
            ans.append(d[i])
                         
        return ans