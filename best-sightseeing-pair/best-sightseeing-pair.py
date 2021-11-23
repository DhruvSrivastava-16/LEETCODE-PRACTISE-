class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_i_sum = values[0]
        max_ans = float('-inf')
        ans = 0
        
        for i in range(1,len(values)):
            
            if values[i]-i+max_i_sum>max_ans:
                max_ans = values[i]-i+max_i_sum
                
            if max_i_sum < values[i]+i:
                max_i_sum = values[i]+i
                
                
        return max_ans
            
            