from collections import deque

class Solution:
    def m_graph(self,wordlist):
        for w in wordlist:
            
            for i in range(len(w)):
                temp = w[:i] + '.' + w[i+1:]
                self.graph[temp].add(w)
        
    
    
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.graph = defaultdict(set)
        wordList += [beginWord]
        self.m_graph(wordList)
        print(self.graph)
        L = len(beginWord)
        dq = deque()
        l=1
        dq.append((beginWord,l))
        visited = set()
        visited.add(beginWord)
        
        while dq:
            
            current_word,l = dq.popleft()
            
            for i in range(L):
                intermediate_word = current_word[:i] + "." + current_word[i+1:]
                
                for w in self.graph[intermediate_word]:
                    
                    
                    if w == endWord:
                        return l+1
                    
                    
                    if w not in visited:
                        visited.add(w)
                        dq.append((w,l+1))
                        
            self.graph[intermediate_word] = []
                        
        return 0
                    
                
        