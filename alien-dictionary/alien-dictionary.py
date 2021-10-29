from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list = defaultdict(set)
        in_degree = {c:0 for word in words for c in word}
        
        for w1, w2 in zip(words,words[1:]):
            for c1, c2 in zip(w1,w2):
                if c1!=c2:
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                        in_degree[c2]+=1
        
        
        
        
        adj_list = defaultdict(set)
        in_degree = {c : 0 for word in words for c in word}
        
        print(in_degree)
        
        for word1, word2 in zip(words,words[1:]):
            for c, d in zip(word1,word2):
                if c!=d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] +=1
                        
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(word2) < len(word1): 
                    return ""
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