class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        freqMap = Counter(nums)
        locMap = defaultdict(int)
        
        for num in nums:
            
            if freqMap[num]==0:
                continue

            elif locMap[num-1]!=0:

                locMap[num-1]-=1
                locMap[num]+=1
                freqMap[num]-=1

            elif freqMap[num+1]>0 and freqMap[num+2]>0:

                locMap[num+2]+=1
                freqMap[num+1]-=1
                freqMap[num+2]-=1
                freqMap[num]-=1

            else:
                return False
                
        return True
                    