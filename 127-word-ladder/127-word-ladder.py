from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        allCombo = defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                
                allCombo[word[:j]+'*'+word[j+1:]].append(word)
                
        
        dq = deque()
        dq.append([beginWord,1])
        visited = set()
        visited.add(beginWord)
        
        while dq:
            
            wrd, stp = dq.popleft()
            
            for j in range(len(wrd)):
                temp = wrd[:j]+'*'+wrd[j+1:]
                
                for wd in allCombo[temp]:
                    
                    if wd == endWord:
                        return stp+1
                    if wd not in visited:
                        visited.add(wd)
                        dq.append([wd,stp+1])
                        
        return 0