class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        hmap = defaultdict(set)
        for word in wordList:
            for loc in range(len(word)):
                
                temp = word[:loc]+"*"+word[loc+1:]
                hmap[temp].add(word)
                
        dq = deque()
        dq.append((beginWord,1))
        visited = set()
        visited.add(beginWord)
        
        while dq:
            
            word, step = dq.popleft()
            
            for loc in range(len(word)):
                
                temp = word[:loc] + "*" + word[loc+1:]

                
                for word2 in hmap[temp]:
                    if word2==endWord:
                        return step+1
                    
                    if word2 not in visited:
                        visited.add(word2)
                        dq.append((word2,step+1))
                    
        return 0
                