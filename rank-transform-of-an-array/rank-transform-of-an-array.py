class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if len(arr)==0:
            return []
        
        temp = arr[:]
        temp.sort()
        rank_map = defaultdict()
        rank = 1
        rank_map[temp[0]] = rank
        
        for i in range(1,len(temp)):
            if temp[i]==temp[i-1]:
                rank_map[temp[i]] = rank
                continue
                
            rank+=1
            rank_map[temp[i]] = rank
            
        print(rank_map)
        ans = []
        for j in arr:
            ans.append(rank_map[j])
            
        return ans
                
                