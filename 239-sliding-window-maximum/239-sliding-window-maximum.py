class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dq = deque()
        
        for itr in range(len(nums)):
            
            while dq and nums[dq[-1][1]]<=nums[itr]:
                dq.pop()
                
            dq.append((nums[itr], itr))
            
            if dq[0][1]==itr-k:
                dq.popleft()
                
            if itr>=k-1:
                answer.append(nums[dq[0][1]])
                
        return answer
