class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        h_map = defaultdict(int)
        stk = []
        
        for log in logs:
            p_id, op, time = log.split(':')
            time = int(time)
            print(type(p_id))
            
                
           
            if op=='start':
                if not stk:
                    stk.append([p_id,time])
                    continue
                    
                print('--',type(stk[-1][0]))
                h_map[stk[-1][0]] += time - stk[-1][1]
                stk[-1][1] = int(time)
                stk.append([p_id,time])

            else:
                print('-',type(p_id))
                h_map[p_id] += time - stk[-1][1]+1
                stk.pop()
                if stk:
                    stk[-1][1] = time+1
                    
        return(h_map.values())
                    
                    
                    
            
        