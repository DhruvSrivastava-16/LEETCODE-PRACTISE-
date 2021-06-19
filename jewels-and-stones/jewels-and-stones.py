class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {}
        
        for i in jewels:
            if i not in jewel_dict:
                jewel_dict[i] = i
                
        count = 0
        for j in stones:
            if j in jewel_dict:
                count+=1
        
        return count