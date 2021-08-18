class Solution:
    def check(self,num):
        print(num)
        if num <1:
            return False
        
        if num == 1:
            return True
        
        if num%3!=0:
            return False
        
        return self.check(num//3)
        
    
    def isPowerOfThree(self, n: int) -> bool:
        return self.check(n)
        