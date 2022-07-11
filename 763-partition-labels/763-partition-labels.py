class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        locMap = dict()
        
        for i in range(len(s)):
            if s[i] not in locMap:
                locMap[s[i]] = [i,i]
                
            else:
                locMap[s[i]][1] = i
                
                
        itr = 0
        itr2 = 0 
        answer = []
        
        
        while itr<len(s):
            
            st = locMap[s[itr]][0]
            end = locMap[s[itr]][1]
            
            itr2 = st
            
            while itr2 < end:
                
                if locMap[s[itr2]][1]>end:
                    end = locMap[s[itr2]][1]
                    
                itr2 += 1
                
            answer.append(end-st+1)
            
            itr=itr2+1
            
        return answer
                
                