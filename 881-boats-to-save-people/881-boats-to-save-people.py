class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        left = 0
        right = len(people)-1
        ans = 0
        
        while left<=right:
            
            ans+=1
            if people[left]+people[right]<=limit:
                left+=1
                
            right-=1
            
        return ans