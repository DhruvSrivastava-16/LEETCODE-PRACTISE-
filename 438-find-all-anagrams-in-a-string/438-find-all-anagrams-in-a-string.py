class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pMap = Counter(p)
        sMap = defaultdict(int)
        window = len(p)
        ans = []
        sz = 0
        
        for i in range(len(s)):
            
            sMap[s[i]]+=1

        
            if i>=window:
                if sMap[s[i-window]]==1:
                    del sMap[s[i-window]]
                    
                else:
                    sMap[s[i-window]]-=1
                    
             
            
                
            if sMap==pMap:
                ans.append(i-window+1)
                
                
            
            
        return ans
        