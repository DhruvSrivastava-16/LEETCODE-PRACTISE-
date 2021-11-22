class Solution:
    
    def helper(self,n,temp,st):
        
        if len(temp)>0:
            temp.append(n)
            print(temp)
            self.ans.append(temp[:])
            temp.pop()
            
        
        for i in range(st,int(n**(0.5))+1):
            if n%i==0:
                temp.append(i)
                self.helper(n//i,temp,i)
                temp.pop()

    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        temp = []
        self.helper(n,temp,2)
        return self.ans        

        