class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque() # stores *indices*
        res = []
        for index, value in enumerate(nums):
            


            while dq and value>=nums[dq[-1]]:
                dq.pop() 

            dq.append(index)

            if dq[0]==index-k:
                dq.popleft()

            if index>=k-1:

                res.append(nums[dq[0]])
                    
        return res
        # for i, cur in enumerate(nums):
        #     while q and nums[q[-1]] <= cur:
        #         q.pop()
        #     q.append(i)
        #     # remove first element if it's outside the window
        #     if q[0] == i - k:
        #         q.popleft()
        #     # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        #     if i >= k - 1:
        #         res.append(nums[q[0]])
        # return res