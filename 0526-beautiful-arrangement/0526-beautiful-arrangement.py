class Solution:
    def countArrangement(self, n: int) -> int:
        global count 
        count = 0
        temp = []
        idx = 1
        self.bt(temp,n,idx)
        return count
        
    def bt(self,temp,n,idx):
        global count
        if len(temp) == n:
            count+=1
            return 
        
        for i in range(1,n+1):
            if i not in temp and (i%idx==0 or idx%i==0):
                temp.append(i)
                idx+=1
                self.bt(temp,n,idx)
                temp.pop()
                idx-=1
                
            