from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h_map = defaultdict(int)
        stk = []
        ans = []
        for i in range(len(nums2)-1,-1,-1):
            
            if not stk:
                
                stk.append(nums2[i])
                ans.append(-1)
                h_map[nums2[i]]=ans[-1]
                
            else:
                if stk[-1]>nums2[i]:
                    
                    ans.append(stk[-1])
                    
                    stk.append(nums2[i])
                    h_map[nums2[i]]=ans[-1]
                    
                else:
                    while stk and stk[-1]<nums2[i]:
                        stk.pop()
                    
                    if not stk:
                        ans.append(-1)
                        
                    else:
                        ans.append(stk[-1])
                        
                    stk.append(nums2[i])
                    h_map[nums2[i]]=ans[-1]
                    
        print(stk,ans,h_map)
        f = []
        for j in nums1:
            f.append(h_map[j])
        return f
            
                    
                
                
            
            