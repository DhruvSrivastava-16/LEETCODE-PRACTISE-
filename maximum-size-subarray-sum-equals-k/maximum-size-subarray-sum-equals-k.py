class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        h_map = defaultdict(int)
        
        r_sum = 0
        longest = 0
        temp = -1
        h_map[0] = 0
        
        for i in range(0,len(nums)):
            
            
            r_sum+=nums[i]
            if r_sum == k:
                longest = i+1
            
            
            if r_sum-k in h_map:
                longest = max(longest,i - h_map[r_sum-k])
                
            if r_sum not in h_map:
                h_map[r_sum] = i
                
        
        print(h_map)
        return longest
                
        