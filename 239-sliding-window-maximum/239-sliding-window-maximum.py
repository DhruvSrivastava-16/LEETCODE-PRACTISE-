class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dq = deque()
        
        for i in range(len(nums)):
            
            while dq and nums[dq[-1][1]]<=nums[i]:
                dq.pop()
                
            dq.append((nums[i],i))
            
            if dq[0][1] <= i-k:
                dq.popleft()
                
            if i>=k-1:
                answer.append(nums[dq[0][1]])
                
        return answer