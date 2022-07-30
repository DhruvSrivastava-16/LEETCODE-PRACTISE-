class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = len(s1)
        st = 0
        comp = Counter(s1)
        freqMap = Counter(s2[:window])
        
        for i in range(0,len(s2)-window+1):
            if comp==freqMap:
                return True
            
            else:
                if freqMap[s2[i]] == 1:
                    freqMap.pop(s2[i])
                    
                else:
                    freqMap[s2[i]] -= 1
            
            
                if i+window<len(s2):
                    if s2[i+window] not in freqMap:
                        freqMap[s2[i+window]] = 1

                    else:
                        freqMap[s2[i+window]] += 1
            
            
        return False