class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dq = deque()
        word_set = set(wordDict)
        dq.append(0)
        visited = set()
        visited.add(0)
        
        while dq:
            
            st = dq.popleft()
            
            for i in range(st+1,len(s)+1):
                if s[st:i] in word_set:
                    if i not in visited:
                        visited.add(i)
                        dq.append(i)
                        
                    if i == len(s):
                        return True
                    
        return False
            