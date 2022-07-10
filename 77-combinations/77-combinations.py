class Solution:
    
    def bt(self,sz,n,temp,answer,pos):
        if len(temp)==sz:
            answer.append(temp[:])
            return 
        
        for i in range(pos,n):
            temp.append(i+1)
            self.bt(sz,n,temp,answer,i+1)
            temp.pop()
            
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        nums = [i for i in range(1,n+1)]
        
        temp = []
        answer = []
        sz = k
        
        self.bt(sz,n,temp,answer,0)
        
        return answer