class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustee = {}
        trusts = {}
        if n == 1:
            return 1
        if len(trust) == 0:
            return -1
        
        for i in trust:
            if i[0] not in trustee:
                trustee[i[0]] = 1
            else:
                trustee[i[0]] += 1
            
            if i[1] not in trusts:
                trusts[i[1]] = 1
            else:
                trusts[i[1]] += 1
        
        print(trustee)
        print(trusts)
        
        for i in range(1,n+1):
            
            if i not in trustee:
                if i in trusts and trusts[i]==n-1:
                    return i
                
        return -1
                
        
        
              
    
        