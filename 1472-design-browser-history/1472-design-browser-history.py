class listNode:
    
    def __init__(self,val=None,back=None,forward=None):
        self.val = val
        self.back = back
        self.next = forward
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = listNode(homepage)
        self.curr = self.head
        
    def visit(self, url: str) -> None:
        
        newNode = listNode(url)
        self.curr.next = newNode
        newNode.back = self.curr
        self.curr = self.curr.next
        
    def back(self, steps: int) -> str:

        while steps and self.curr.back:
            self.curr = self.curr.back
            steps-=1
            
        return self.curr.val
   

    def forward(self, steps: int) -> str:
        
        count = 0
        
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps-=1
            
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)