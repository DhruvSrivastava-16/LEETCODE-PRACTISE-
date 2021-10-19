from collections import defaultdict

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        h_map = defaultdict(int)
        p_stack = []
        
        for log in logs:
            p_id, mode, time = log.split(':')
            time=int(time)
            #print(type(p_id), mode, type(time))
            
            if mode=='start':
                
                if not p_stack:
                    p_stack.append([p_id,time])
                    
                else:
                    h_map[p_stack[-1][0]]+=time-p_stack[-1][1]
                    print("UP; Adding time to",p_stack[-1][0],time-p_stack[-1][1])
                    p_stack.append([p_id,time])
                    
            else:
                print(p_stack)
                p_pid, end_t = p_stack.pop()
                if len(p_stack)!=0:
                    print('time updated',time)
                    p_stack[-1][1]=time+1
                print('p_stack after pop:',p_stack)
                print('ending:',p_pid,end_t,time)
                print("PP; Adding time to",p_pid,time-end_t+1)

                h_map[p_pid]+=time-end_t+1
               
        print(h_map)
        answer = []
        for k,v in h_map.items():
            answer.append(v)
            
        return answer
        