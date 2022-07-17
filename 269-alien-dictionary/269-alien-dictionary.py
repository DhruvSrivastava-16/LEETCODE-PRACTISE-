class Solution:
    
    def dfs(self,n,graph,stk,recvStk,visited):
        visited.add(n)
        recvStk[n]=True
        for ne in graph[n]:
            if ne not in visited:
                self.dfs(ne,graph,stk,recvStk,visited)
                
            elif recvStk[ne]==True:
                self.cycle = True
                
        recvStk[n] = False
        stk.append(n)
    
    def alienOrder(self, words: List[str]) -> str:
        
        
        graph = defaultdict(list)
        nodes = set()
        
#         for word in words:
            
#             for i in range(0,len(word)-1):
                
#                 if word[i]==word[i+1]:
#                     continue
                    
#                 graph[word[i]].add(word[i+1])
#                 nodes.add(word[i])
#                 nodes.add(word[i+1])
        # nodes = {c : [] for word in words for c in word}
        for word in words:
            for c in word:
                nodes.add(c)
        for first_word, second_word in zip(words, words[1:]):
        
            for c, d in zip(first_word, second_word):

                if c != d: 
                    graph[c].append(d)

                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""

        stk = []
        recvStk = dict()
        visited = set()
        self.cycle = False
        
        for n in nodes:
            if n not in visited:
                self.dfs(n,graph,stk,recvStk,visited)
                
            if self.cycle:
                print('cycle')
                return ""
        print('AG:',graph)    
        print(graph,stk,nodes)

        return (''.join(stk[::-1]))

    # def alienOrder(self, words: List[str]) -> str:

        # Step 0: Put all unique letters into the adj list.
#         reverse_adj_list = {c : [] for word in words for c in word}

#         # Step 1: Find all edges and put them in reverse_adj_list.
#         for first_word, second_word in zip(words, words[1:]):
            
#             for c, d in zip(first_word, second_word):
#                 print(c,d)
#                 if c != d: 
#                     reverse_adj_list[d].append(c)
#                     break
#             else: # Check that second word isn't a prefix of first word.
#                 if len(second_word) < len(first_word): 
#                     return ""
        
#         print(reverse_adj_list)
#         # Step 2: Depth-first search.
#         seen = {} # False = grey, True = black.
#         output = []
#         def visit(node):  # Return True iff there are no cycles.
#             if node in seen:
#                 return seen[node] # If this node was grey (False), a cycle was detected.
#             seen[node] = False # Mark node as grey.
#             for next_node in reverse_adj_list[node]:
#                 result = visit(next_node)
#                 if not result: 
#                     return False # Cycle was detected lower down.
#             seen[node] = True # Mark node as black.
#             output.append(node)
#             return True

#         if not all(visit(node) for node in reverse_adj_list):
#             return ""

#         return "".join(output)