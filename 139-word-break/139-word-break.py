from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dq = deque()
        dq.append(0)
        wordSet = set(wordDict)
        visited = set()
        
        while dq:
            
            st = dq.popleft()
            if st in visited:
                continue
                
            for end in range(st+1,len(s)+1):
                if s[st:end] in wordSet:
                    dq.append(end)
                    if end == len(s):
                        return True
                    
            visited.add(st)
                    
        return False
            
            
            