class Solution():
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
	
        f_inc = [1] * n   # stores count for increasing sub sequences
        f_dec = [1] * n   # stores count for decreasing sub sequences

        for k in range(1, 3):
            for i in range(0, n):
                f_inc[i] = 0
                f_dec[i] = 0
                for j in range(i+1, n):
                    if rating[j] > rating[i]:
                        f_inc[i] += f_inc[j]
                    else:
                        f_dec[i] += f_dec[j]
        return sum(f_inc) + sum(f_dec)