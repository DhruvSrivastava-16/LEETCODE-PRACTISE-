class ListNode:
    def __init__(self, val = 0, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.next = nxt
class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = ListNode(homepage)
        self.last = self.node

    def visit(self, url: str) -> None:
        self.last.next = ListNode(url)
        self.last.next.prev = self.last
        self.last = self.last.next

    def back(self, steps: int) -> str:
        while steps and self.last.prev:
            steps -=1
            self.last = self.last.prev
        return self.last.val
            

    def forward(self, steps: int) -> str:
        while steps and self.last.next:
            steps -=1
            self.last = self.last.next
        return self.last.val
            
