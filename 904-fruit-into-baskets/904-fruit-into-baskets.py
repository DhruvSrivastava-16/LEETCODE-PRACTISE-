class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxxShift = 0
        seen = dict()
        answer = 0
        
        
        while right<len(nums):
            
            if nums[right] not in seen:
                if len(seen)==2:
                    
                    key = list(seen.keys())
                    
                    if seen[key[0]]>seen[key[1]]:
                        dontKeep = key[1]
                        keep = key[0]
                    else:
                        keep = key[1]
                        dontKeep = key[0]

                     
                    left = seen.pop(dontKeep)+1
                    # left = seen[keep]
                    

            seen[nums[right]]=right
                
            answer = max(answer,right-left+1)
            right+=1
            
        return(answer)
            
                        