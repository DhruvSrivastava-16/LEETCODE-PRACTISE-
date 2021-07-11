
class Solution:
    def threeSum(self, nums):
        ans = []
        finish = {}
        nums.sort()
        done = {}
        k = 0
        for i in range(0,len(nums)-1):
            print(i,nums[i])
            if nums[i] in done:
                continue
            
            else:
                temp_ans=[]
               
                temp_sum = k-nums[i] 
                
                st = i+1
                end = len(nums)-1
                while st<end and nums[i] not in done:
                    #print("st: ",st,"end: ",end)
                    if nums[st] + nums[end] > temp_sum:
                        end-=1
                    elif  nums[st] + nums[end] < temp_sum:
                        st+=1
                    else:
                        if (nums[i],nums[st],nums[end]) not in finish:
                            finish[(nums[i],nums[st],nums[end])] = 1
                            ans.append([nums[i],nums[st],nums[end]])
                        end-=1
                        st+=1
                done[nums[i]] = 1
        print(done)
        return(ans)