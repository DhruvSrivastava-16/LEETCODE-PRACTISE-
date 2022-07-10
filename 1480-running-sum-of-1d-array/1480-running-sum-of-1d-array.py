class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        answer = []
        
        for i in range(len(nums)):
            runningSum+=nums[i]
            answer.append(runningSum)
            
        return answer
            