from collections import defaultdict
class Solution:
    
    def dfs(self, graph, k, v, CC, visited):
        CC.append(k)
        visited.add(k)
        for n in graph[k]:
            if n not in visited:
                self.dfs(graph, n, v, CC, visited)
        
        
        
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        nameMap = defaultdict(set)
        
        for account in accounts:
            for itr in range(1,len(account)):
                tempSet = set(account[1:])
                tempSet.remove(account[itr])
                graph[account[itr]]=graph[account[itr]].union(tempSet)
                nameMap[account[itr]] = account[0]
        
        visited = set()
        CC = []
        answer = []
        for k,v in graph.items():
            CC = []
            if k not in visited:

                self.dfs( graph, k, v, CC, visited)

                answer.append(CC[:])
                

        final_answer = []
        temp = []

        for ans in answer:
            temp = []
            temp.append(nameMap[ans[0]])
            ans.sort()
            temp += ans[0:]
            final_answer.append(temp[:])

        return(final_answer)
        
            
            