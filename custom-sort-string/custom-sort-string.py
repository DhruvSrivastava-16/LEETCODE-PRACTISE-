from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = ''
        h_map = Counter(s)
        for i in order:
            if i in h_map:
                answer+=h_map[i]*i
                h_map[i] = -1
                
        for k, v in h_map.items():
            if v!=-1:
                answer+=k*v
                
        return answer
        
        