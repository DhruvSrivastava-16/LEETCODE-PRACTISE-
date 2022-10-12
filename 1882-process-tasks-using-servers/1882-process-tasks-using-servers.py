class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        
        server_store = []
        for itr in range(len(servers)):
            heapq.heappush(server_store,(servers[itr],itr))
            
        answer = []
        task_store = []
        time = 0
        
        for itr in range(len(tasks)):
            time = max(time,itr)
            
            if not server_store:
                
                time = task_store[0][0]
                
            while task_store and task_store[0][0]<=time:
                server = heapq.heappop(task_store)[1]
                heapq.heappush(server_store,server)
                
            answer.append(server_store[0][1])
            
            heapq.heappush(task_store,(time+tasks[itr],heapq.heappop(server_store)))
                
        return answer