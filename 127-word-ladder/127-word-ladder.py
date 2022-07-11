from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        hmap = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i+1:]
                hmap[temp].append(word)
                
        dq = deque()
        dq.append((beginWord,1))
        visited = set()
        visited.add(beginWord)
        step = 0
        
        while dq:
            
            word, step = dq.popleft()
            
            
            for i in range(len(beginWord)):
                temp = word[:i]+'*'+word[i+1:]
                
                for wrd in hmap[temp]:
                    
                    if wrd == endWord:
                        return step+1
                    
                    if wrd not in visited:
                        visited.add(wrd)
                        dq.append((wrd,step+1))
            
        return 0
            
            