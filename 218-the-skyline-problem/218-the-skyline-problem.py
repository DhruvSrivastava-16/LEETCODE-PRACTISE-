class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        edges = []
        
        for itr in range(len(buildings)):
            
            edges.append((buildings[itr][0],itr))
            edges.append((buildings[itr][1],itr))
            
        edges.sort()
            
        answer = []
        
        idx = 0
        
        live = []
        
        while idx<len(edges):
            
            curr = edges[idx][0]
            
            while idx<len(edges) and edges[idx][0]==curr:
                
                itr = edges[idx][1]
                
                if buildings[itr][0] == curr:
                    r = buildings[itr][1]
                    height = buildings[itr][2]
                    heapq.heappush(live, [-height, r])
                    
                while live and live[0][1] <= curr:
                    heapq.heappop(live)
                idx += 1
            
            # Get the maximum height from 'live'.
            max_height = -live[0][0] if live else 0
            
            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([curr, max_height])
                
        return answer