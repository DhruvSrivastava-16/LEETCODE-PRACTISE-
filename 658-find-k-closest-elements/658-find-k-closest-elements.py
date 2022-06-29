import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        store = []
        for num in arr:
            store.append([abs(num-x),num])
        
        store.sort(key = lambda x:x[0])
        print(store)
        temp = [store[itr][1] for itr in range(k)]
        temp.sort()
        return temp
            
            