class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dq = deque()
        visited = set()
        
        dq.append(0)
        visited.add(0)
        wordS = set(wordDict)
        
        while dq:
            
            
            st = dq.popleft()
            
            if st == len(s):
                return True
            
            for i in range(st+1,len(s)+1):
                
                if s[st:i] in wordS:
                    if i not in visited:
                        visited.add(i)
                        dq.append(i)
                    
        return False
