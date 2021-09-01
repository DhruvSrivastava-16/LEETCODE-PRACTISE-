class Solution:
    def factorial(self,n):
        if n==0:
            return 1
        
        if n==1:
            return 1
        
        return n*self.factorial(n-1)
    
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        
        n = self.factorial(n)
        #print('N! = ',n)
        
        while True and n>0:
            #print('n%10 ',n%10)
            if n%10 == 0:
                count+=1
                n = n//10
                
            
            else:
                break
    
        return count