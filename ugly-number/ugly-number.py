class Solution:
    def isUgly(self, n: int) -> bool:
        while n>0 and n%2==0:
            n=n//2
        while n>0 and n%3==0:
            n=n//3
        while n>0 and n%5==0:
            n=n//5
        if n==1:
            return True
        return False
        