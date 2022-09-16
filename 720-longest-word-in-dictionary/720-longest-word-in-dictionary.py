class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self, wr):
        node = self
        
        for w in wr:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.isEnd = True
        
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        node = Trie()
        
        for wr in words:
            node.addWord(wr)
          
        def dfs(node, s):
            if node.isEnd:
                if len(lrWr) == 0:
                    lrWr.append(s)
                else:
                    while(lrWr and len(s) > len(lrWr[-1])):
                        lrWr.pop()
                        
                    if len(lrWr) == 0 or len(lrWr[-1]) == len(s):
                        lrWr.append(s)
            else:
                return
                    
            for i in node.children:
                dfs(node.children[i], s+i)
        
        lrWr = []
        for i in node.children:
            dfs(node.children[i], i)
            
        lrWr.sort()
        
        return lrWr[0] if lrWr else ""