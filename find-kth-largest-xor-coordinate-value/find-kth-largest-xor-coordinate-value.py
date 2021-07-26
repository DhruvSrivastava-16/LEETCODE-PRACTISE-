class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        dp = []
        for i in range(len(matrix)):
            x = []
            for j in range(len(matrix[0])):
                x.append(0)
            dp.append(x)
            
            
        for i in range(len(matrix)):
            c = 0
            for j in range(len(matrix[0])):
                c ^= matrix[i][j]
                if j == 0:
                    if i == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = dp[i-1][j] ^ matrix[i][j]
                else:
                    if i == 0:
                        dp[i][j] = c
                    else:
                        dp[i][j] = c ^ dp[i-1][j]
						
        l = []
        for i in dp:
            l += i
        return sorted(l,reverse=True)[k-1]