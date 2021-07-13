class Solution:
    def split(self,num):
        a = 0
        while num>0:
            t = num%10
            a = a + t**2
            
            num = num//10
        return a
        
    def isHappy(self, n: int) -> bool:
        visited = {}
        num = n
        while True:
            visited[num] = 1
            num = self.split(num)
            if num == 1:
                return True
            
            print(visited)
            
            if num in visited:
                return False
            
            
            
            
            
            
        
            
        