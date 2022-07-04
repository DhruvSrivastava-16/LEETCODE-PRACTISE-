from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
         
        sz = len(beginWord)
        
        allComb = defaultdict(list)
        
        for word in wordList:
            for j in range(sz):
                allComb[word[:j]+"."+word[j+1:]].append(word)
                
                
        dq = deque()
        
        dq.append([beginWord,1])
        visited = set()
        
        visited.add(beginWord)
        
        while dq:
            
            wrd, stp = dq.popleft()
            
            for i in range(sz):
                temp = wrd[:i]+'.'+wrd[i+1:]
                for w in allComb[temp]:
                    if w == endWord:
                        return stp+1
                    
                    if w not in visited:
                        visited.add(w)
                        dq.append([w,stp+1])
        return 0
                