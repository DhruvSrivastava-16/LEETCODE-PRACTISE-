class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        totalSum = 0
        for num in nums:
            totalSum+=num
            
        maxArrSum = totalSum-x
        print('mx:',maxArrSum)
        low = 0
        high = 0
        Ans = False
        currSum = 0
        sz = 0
        
        while high<len(nums):
            currSum+=nums[high]
            
            while currSum>maxArrSum and low<=high:
                currSum-=nums[low]
                low+=1
                
            if currSum == maxArrSum:
                Ans = True
                print(low,high,'found')
                sz = max(high-low+1,sz)
            print('curr',currSum)
                
            

            high+=1
                
            
        if Ans:
            return len(nums)-sz
        
        return -1
            
            