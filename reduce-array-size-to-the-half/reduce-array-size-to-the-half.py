from collections import Counter
import heapq as hq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_Counter = Counter(arr)
        heap_m = []
        
        for i in arr_Counter.keys():
            heap_m.append([-arr_Counter[i],i])
            
        hq.heapify(heap_m)
        initial_len = len(arr)
        curr_len = len(arr)
        ans = set()
        
        while True:
            top = hq.heappop(heap_m)
            curr_freq = top[0]
            
            curr_len = curr_len + curr_freq
            ans.add(top[1])
            
            if curr_len <= (initial_len)//2:
                break
                
        print(ans)
        return len(ans)
                