from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
        
        for word1, word2 in zip(words,words[1:]):
            for c, d in zip(word1,word2):
                if c!=d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] +=1
                        
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(word2) < len(word1): return ""
            ""
                    
        print(in_degree,adj_list)
        
      

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)