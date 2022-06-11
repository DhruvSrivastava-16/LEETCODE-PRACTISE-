class Solution:
    
    def BT(self, candidates, answerSet, temp, target, summ, st):
        if summ == target:
            # temp2 = sorted(temp)
            # if temp2 not in answerSet:
            
            answerSet.append(temp[:])
            
        for i in range(st,len(candidates)):
            if summ+candidates[i]<=target:
                summ += candidates[i]
                temp.append(candidates[i])
                self.BT(candidates, answerSet, temp, target, summ, i)
                summ -= candidates[i]
                temp.pop()
                
        # return 
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answerSet = []
        self.BT(candidates, answerSet, [], target, 0, 0)
        return answerSet