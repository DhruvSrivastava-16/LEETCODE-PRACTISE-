class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        hmap = defaultdict(int)
        
        left = 0
        right = 0
        answer = float('-inf')
        
        while left<=right and right<len(s):
            if s[right] not in hmap:
                if not hmap:
                    left = right
                    hmap[s[right]] = right
                
                elif len(hmap)==2:
                    keys = list(hmap.keys())
                    
                    first = keys[0]
                    second = keys[1]
                    
                    if hmap[first]<hmap[second]:  
                        left = hmap.pop(first) + 1
                        
                    else:
                        left = hmap.pop(second) + 1
                        
            
            hmap[s[right]] = right
                    
            # print('RL:',right-left+1,hmap)        
            answer = max(answer,right-left+1)
            right+=1
            
        return answer
                    