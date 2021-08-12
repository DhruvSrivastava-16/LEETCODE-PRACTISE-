class Solution:
    def canPartition(self, value: List[int]) -> bool:
        weight = [i for i in value]
        total_sum = 0
        for i in value:
            total_sum += i
            
        if total_sum%2!=0:
            return False
        
        target = total_sum//2
  
        
        dp = [[0 for i in range(target+1)] for j in range(len(value)+1)]
        F = False
        
        for i in range(len(value)+1):
            if F:
                break
            for j in range(target+1):

                if i==0 or j==0:
                    dp[i][j] = 0

                elif weight[i-1]>j:
                        dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = max(value[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])

                if dp[i][j] == target:
                   
                    return True
                
        return False
            