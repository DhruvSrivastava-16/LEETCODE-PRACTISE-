class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.words = []

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            curr.words.append(word)
            
    def search(self,typed):
        curr = self.root
        
        for char in typed:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            
        return curr.words
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for word in products:
            trie.insert(word)
            
        answer = []
        
        for i in range(len(searchWord)):
            temp = trie.search(searchWord[:i+1])
            if temp:
                answer.append(sorted(temp)[:3])
            else:
                answer.append([])
                
        return answer
            
            