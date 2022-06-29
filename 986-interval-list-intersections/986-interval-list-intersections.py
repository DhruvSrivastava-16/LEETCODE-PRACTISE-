class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        
        itr = 0
        itr1 = 0 
        itr2 = 0
        curr = []
      
        answer = []
      
              
        while itr1<len(fl) and itr2<len(sl):
            
            lo, hi = max(fl[itr1][0],sl[itr2][0]),min(fl[itr1][1],sl[itr2][1])
            
            if lo<=hi:
                answer.append([lo,hi])

            if fl[itr1][1]<=sl[itr2][1]:
                itr1+=1
                
            else:
                itr2+=1
            
            
            

            
        return answer
            
        
              
              