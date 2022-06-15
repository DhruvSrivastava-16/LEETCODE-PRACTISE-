from collections import defaultdict
class Solution:
    
    def dfs(self,n,visited,richerThanX,graph):
        visited.add(n)
        richerThanX.append(n)
        for ne in graph[n]:
            if ne not in visited:
                self.dfs(ne,visited,richerThanX,graph)
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        richMap = dict()
        for rich in richer:
            graph[rich[1]].append(rich[0])
            
        richerThanX = []
        
        for n in range(len(quiet)):
            visited = set()
            richerThanX = []
            self.dfs(n,visited,richerThanX,graph)
            richMap[n] = richerThanX
            print(richerThanX)
            
        print(richMap)
        ans = []
        
        for k,v in richMap.items():
            temp = quiet[k]
            tempans = k
            for itr in v:
                
                if temp >= quiet[itr]:
                    tempans = itr
                    temp = quiet[itr]
                    
            ans.append(tempans)
            
        return ans