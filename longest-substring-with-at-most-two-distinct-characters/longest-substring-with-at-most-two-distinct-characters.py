class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        h_map = dict()
        left = 0
        right = 0
        max_len = float('-inf')
        
        while right<len(s):
            
            h_map[s[right]] = right
            right+=1
            
            if len(h_map)>2:
                
                del_idx = min(h_map.values())
                del h_map[s[del_idx]]
                left = del_idx+1
                
            max_len = max(right-left,max_len)
            
            
        return max_len
                