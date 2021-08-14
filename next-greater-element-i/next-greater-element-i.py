class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        mst  = []
        
        for i in range(0,len(nums2)):
            hmap[nums2[i]] = i
        
        for j in nums2:
            if len(mst)<=0:
                mst.append(j)
                
            elif mst[-1]<j:
                    
                    while len(mst)>0 and mst[-1]<j:
                        print('MST:',mst)
                        temp = mst.pop()
                        hmap[temp] = j
            
            mst.append(j)
                        
                        
        print(hmap)
        print(mst)
        while len(mst)>0:
            temp = mst.pop()
            hmap[temp] = -1
                    
        ans = []
        print(hmap)
        for i in nums1:
            ans.append(hmap[i])
            
        return(ans)
