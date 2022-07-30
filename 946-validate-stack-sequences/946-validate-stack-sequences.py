class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        popItr = 0
        pushItr = 0
        stack = []
        
        
        while pushItr<len(pushed):
            stack.append(pushed[pushItr])
            while stack and stack[-1]==popped[popItr]:
                stack.pop()
                popItr+=1
                
            pushItr+=1
                
        return len(stack)==0
