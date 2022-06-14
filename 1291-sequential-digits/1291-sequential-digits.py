class Solution:
    
    def recursion(self,arr,nums,high):
        if int(nums)>high:
            return 
        
        if int(nums) not in arr:
            arr.add(int(nums))
            
        if nums[-1]==str(9):
            nums = ''.join([str(i) for i in range(1,len(nums)+2)])
            arr.add(int(nums))
        
        for j in range(int(nums[-1])+1,10):
            nums += str(j)
            self.recursion(arr,nums,high)
            

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = set()
        for i in range(1,10):
            temp = str(i)
            self.recursion(arr,temp,high)
        
        fans = []
        for j in arr:
            if j>=low and j<=high:
                fans.append(j)
        
        fans.sort()
        
        return list(fans)