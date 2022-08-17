class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        st = 0
        dq = deque()
        seen = set()
        wordSet = set(wordDict)
        dq.append(0)
        seen.add(0)
        
        
        while dq:
            
            st = dq.popleft()
            
            for end in range(st+1,len(s)+1):
                if end not in seen:
                    temp = s[st:end]
                    if temp in wordSet:
                        if end==len(s):
                            return True
                        
                        dq.append(end)
                        seen.add(end)
                        
        return False
                
#         st = 0
#         dq = deque()
#         dq.append(0)
#         wordSet = set(wordDict)
#         visited = set()
#         visited.add(0)
        
#         while dq: 
            
            
#             st = dq.popleft()
            
#             for end in range(st+1,len(s)+1):
#                 temp = s[st:end]
#                 if temp in wordSet and end not in visited:
                    
#                     if end == len(s):
#                         return True
                    
#                     dq.append(end)
#                     visited.add(end)
            
#         return False