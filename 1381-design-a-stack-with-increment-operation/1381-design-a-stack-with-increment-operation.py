class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.max = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stk)>=self.max:
            return 
        
        self.stk.append(x)
        

    def pop(self) -> int:
        
        if not self.stk:
            return -1
        
        top = self.stk.pop()
        
        return top
        

    def increment(self, k: int, val: int) -> None:
        
        
        for i in range(k):
            if i>=len(self.stk):
                return 
            
            self.stk[i]+=val
            
        return


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)