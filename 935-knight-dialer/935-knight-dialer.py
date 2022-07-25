class Solution:
    def knightDialer(self, n: int) -> int:
        
        hash={}
        hash[1]=[6,8]
        hash[2]=[7,9]
        hash[3]=[4,8]
        hash[4]=[0,3,9]
        hash[5]=[]
        hash[6]=[0,1,7]
        hash[7]=[2,6]
        hash[8]=[1,3]
        hash[9]=[2,4]
        hash[0]=[4,6]
        
        dp=[[0 for i in range(10)] for j in range(n+1)]
        
        for i in range(n+1):
            for j in range(10):
                if i==0:
                    dp[i][j]=0
                elif i==1:
                    dp[i][j] = 1
                else:
                    sm=0
                    for x in hash[j]:
                        sm+=dp[i-1][x]
                    dp[i][j]=sm
                    
        return sum(dp[n])%(10**9+7)
        