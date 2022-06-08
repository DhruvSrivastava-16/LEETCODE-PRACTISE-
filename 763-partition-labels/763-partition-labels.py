from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hmap = dict()
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = [i,i]
                
            else:
                hmap[s[i]][1] = i
         
        partitions = []
        itr = 0
        part = 0
        
        
        while itr<len(s):
            
            st = hmap[s[itr]][0]
            end = hmap[s[itr]][1]
            itr2 = st
            
            while itr2<end:
                
                if hmap[s[itr2]][1]>end:
                    end = hmap[s[itr2]][1]
                    
                itr2+=1
                
            partitions.append(end-st+1)
            itr = itr2 + 1
            
        return(partitions)
                    
            
            
        
        
        
        