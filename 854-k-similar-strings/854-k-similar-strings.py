class Solution:
    
    def getChildren(self,curr,target,seen):
        
        children = []
        s = list(curr)
        i = 0  # first index s.t. curr[i] != target[i]
        while curr[i] == target[i]:
            i += 1

        for j in range(i + 1, len(s)):
            if s[j] == target[i]:
                s[i], s[j] = s[j], s[i]
                children.append(''.join(s))
                s[i], s[j] = s[j], s[i]

        return children

    def kSimilarity(self, s1: str, s2: str) -> int:
        
        dq = deque()
        dist = 0
        
        seen = set()
        seen.add(s1)
        
        dq.append((s1,dist))
        
        while dq:
            
            
            temp, level = dq.popleft()
            # print(temp,dq)
            
            if temp == s2:
                return level
            
            children = self.getChildren(temp,s2,seen)
            
            for child in children:
                if child not in seen:
                    dq.append((child,level+1))
                    seen.add(child)
                
        
            
            
            
            