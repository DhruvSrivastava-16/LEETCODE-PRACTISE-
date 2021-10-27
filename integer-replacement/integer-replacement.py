class Solution:
    def count(self,n,count):
        if n==1:
            return count
        
        if n%2==0:
            return self.count(n//2,count+1)
        
        else:
            return min(self.count(n+1,count+1),self.count(n-1,count+1))
    
    def integerReplacement(self, n: int) -> int:
        return self.count(n,0)
        