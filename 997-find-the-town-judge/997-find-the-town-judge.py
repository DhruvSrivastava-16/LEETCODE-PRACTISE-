from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        if len(trusts)==0 and n==1:
            return n
        
        h_map = defaultdict(list)
        h_map_self = defaultdict(list)
        for trust in trusts:
            h_map[trust[1]].append(trust[0])
            h_map_self[trust[0]].append(trust[1])
            
        print(h_map)
        
        for k, v in h_map.items():
            
            if len(v)==n-1 and k not in h_map_self:
                return k
            
            
        return -1