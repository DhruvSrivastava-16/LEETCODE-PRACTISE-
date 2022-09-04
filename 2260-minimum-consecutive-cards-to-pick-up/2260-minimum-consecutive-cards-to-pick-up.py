class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        locMap = defaultdict(int)
        answer = float('inf')
        left, right = 0, 0
        
        while left<=right and right<len(cards):
            
            if cards[right] not in locMap:
                locMap[cards[right]] = right
                
            else:
                
                answer = min(answer,right-locMap[cards[right]]+1)
                
                while left<=locMap[cards[right]]:
                    locMap.pop(cards[left])
                    left+=1
                    
                locMap[cards[right]] = right
            right+=1
        
        if answer == float('inf'):
            return -1
        
        return answer
    
                
        