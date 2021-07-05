class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    
        d = {}
        for i in words:
            if i in d:
                d[i] = d[i] - 1
            
            else:
                d[i] = -1
        
        print(d)
        a =[]
        for ke,v in d.items():
            a.append((int(v),ke))
        
        heapq.heapify(a)
        print(a)
        
        an = heapq.nsmallest(k,a)
        
        
        ans = []
        for i in an:
            ans.append(i[1])
            
        return ans