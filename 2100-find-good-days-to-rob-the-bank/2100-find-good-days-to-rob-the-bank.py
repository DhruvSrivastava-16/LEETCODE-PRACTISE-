class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        
        dec = [None for i in range(0,len(security))]
        inc = [None for i in range(0,len(security))]
        
        dec[-1] = (0,security[-1])
        inc[0] = (0,security[0])
        
        for itr in range(len(security)-2,-1,-1):
            
            if dec[itr+1][1]>=security[itr]:
                dec[itr] = (dec[itr+1][0]+1,security[itr])
                
            else:
                dec[itr] = (0,security[itr])
                
        # print(dec)

        for itr in range(1,len(security)):
            
            if inc[itr-1][1]>=security[itr]:
                inc[itr] = (inc[itr-1][0]+1,security[itr])
                
            else:
                inc[itr] = (0,security[itr])
        
        answer = []
        
        for itr in range(len(security)):
            
            if dec[itr][0]>=time and inc[itr][0]>=time:
                answer.append(itr)
                
        return answer