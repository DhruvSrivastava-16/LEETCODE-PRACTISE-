class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    
        freq = [0]*26
        for i in tasks:
            freq[ord(i) - ord('A')] += 1
        
        freq.sort()
        
        print(freq)
        
        
        f_max = freq.pop()
        
        ideal_time = (f_max - 1)*n 
        
        while freq and ideal_time>0:
            t = freq.pop()
            ideal_time = ideal_time - min(f_max-1,t)
        
        ideal_time = max(0,ideal_time)
            
        print(freq)
        return ideal_time + len(tasks)
            
        