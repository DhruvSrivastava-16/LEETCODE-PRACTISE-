class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        itr = 0
        pMap = Counter(p)
        ans = []
        sMap = defaultdict(int)
        
        window = len(p)
        
        for i in range(len(s)):
            
            sMap[s[i]] += 1
            
            if i>=window:
                
                if sMap[s[i-window]] == 1:
                    del sMap[s[i-window]]
                    
                else:
                    sMap[s[i-window]]-=1
                    
                    
                    
            if sMap==pMap:
                ans.append(i-window+1)
                
                
        return ans
            
            
            
            
            