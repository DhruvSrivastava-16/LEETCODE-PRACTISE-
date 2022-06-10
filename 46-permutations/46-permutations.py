class Solution:
    
    def backtracking(self, nums, temp, i,ans,vis):
        vis.add(i)

        if len(temp)==len(nums):
            ans.append(temp[:])
            return 
        
        
        for j in range(0,len(nums)):
            if j not in vis:
                temp.append(nums[j])
                self.backtracking(nums,temp,j,ans,vis)
                temp.pop()
                vis.remove(j)
                
        
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0,len(nums)):
            temp = []
            vis = set()
            temp.append(nums[i])
            print(i,temp)
            self.backtracking(nums,temp,i,ans,vis)
            
        return ans