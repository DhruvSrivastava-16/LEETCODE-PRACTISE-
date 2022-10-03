class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        start = "0000"
        seen = set()
        dq = deque()
        dq.append((start,0))
        deadSet = set(deadends)
        seen.add(start)
        
        if target==start:
            return 0
        
        while dq:
            
            node, level = dq.popleft()
            
            if node not in deadSet:
                
                seen.add(node)
                
                for d in (-1,1):
                    for itr in range(4):

                        left = node[:itr]
                        curr = int(node[itr])
                        right = node[itr+1:]
                        
                        if d == 1:
                            if curr==9:
                                curr = 0
                            
                            else:
                                curr+=1
                                
                        else:
                            if curr==0:
                                curr = 9
                                
                            else:
                                curr-=1
                                
                        final = left+str(curr)+right
                        
                        if final == target:
                            return level+1
                        
                        if final not in seen:
                            dq.append((final,level+1))
                            seen.add(final)
                                
        return -1
                                
                        