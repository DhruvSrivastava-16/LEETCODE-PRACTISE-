class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        # DP approach: iterate through all of the input chars
        # maintain min number of flips to end with 0 or with 1
        flips_0 = 0
        flips_1 = 0
        
        for i, c in enumerate(S):
            if c == '0':
                # flips_0 stays the same
                flips_1 = min(flips_0, flips_1) + 1
                
            elif c == '1':
                flips_1 = min(flips_0, flips_1)
                flips_0 += 1
        
        return min(flips_0, flips_1)